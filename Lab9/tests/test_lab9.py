"""Lab 9 automated tests. Run from the project folder:  python -m unittest discover -s tests -t ."""
import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from BulkDiscount import BulkDiscount
from DigitalProduct import DigitalProduct
from DiscountStrategy import DiscountStrategy
from helpers import get_positive_float, load_products
from Inventory import Inventory
from NoDiscount import NoDiscount
from Order import Order
from OrderLine import OrderLine
from PercentageDiscount import PercentageDiscount
from PhysicalProduct import PhysicalProduct
from Product import Product
from ProductFactory import ProductFactory
from StudentDiscount import StudentDiscount
from Supplier import Supplier

CSV_TEXT = (
    "product_type,product_id,name,price,stock_quantity\n"
    "physical,P001,Desk Lamp,25.00,10\n"
    "digital,D001,Photo Editor,49.90,100\n"
    "service,S001,Installation,30.00,5\n"
    "physical,P002,Office Chair,abc,3\n"
    "physical,P003,Monitor Stand,39.50,7\n"
)


def make_supplier() -> Supplier:
    return Supplier("S001", "TechSource", "sales@techsource.com")


def make_order_total_250(discount=None) -> Order:
    order = Order("ORD001", discount)
    product = ProductFactory.create("physical", "001", "Desk", 125.0, 10, make_supplier())
    order.add_order_line(product, 2)  # 2 x 125 = 250
    return order


class TestDiscountStrategies(unittest.TestCase):
    def test_no_discount_returns_total_unchanged(self):
        self.assertEqual(NoDiscount().apply(250), 250)

    def test_percentage_discount(self):
        self.assertAlmostEqual(PercentageDiscount(10).apply(250), 225)

    def test_bulk_discount_at_and_above_threshold(self):
        self.assertEqual(BulkDiscount(200, 20).apply(250), 230)
        self.assertEqual(BulkDiscount(200, 20).apply(200), 180)

    def test_bulk_discount_below_threshold(self):
        self.assertEqual(BulkDiscount(200, 20).apply(199), 199)

    def test_student_discount(self):
        self.assertAlmostEqual(StudentDiscount().apply(100), 95)

    def test_all_strategies_are_discount_strategies(self):
        for strategy in (NoDiscount(), PercentageDiscount(5), BulkDiscount(1, 1), StudentDiscount()):
            self.assertIsInstance(strategy, DiscountStrategy)

    def test_base_class_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            DiscountStrategy()  # abstract


class TestOrderUsesStrategy(unittest.TestCase):
    def test_default_is_no_discount(self):
        self.assertEqual(make_order_total_250().calculate_total(), 250)

    def test_order_uses_given_strategy(self):
        order = make_order_total_250(BulkDiscount(200, 20))
        self.assertEqual(order.calculate_total(), 230)

    def test_set_discount_changes_strategy(self):
        order = make_order_total_250(BulkDiscount(200, 20))
        self.assertEqual(order.calculate_total(), 230)
        order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(order.calculate_total(), 225)

    def test_new_strategy_works_without_changing_order(self):
        class HalfPrice(DiscountStrategy):  # defined here: Order is untouched
            def apply(self, total: float) -> float:
                return total / 2

        self.assertEqual(make_order_total_250(HalfPrice()).calculate_total(), 125)

    def test_order_source_has_no_discount_branching(self):
        with open("Order.py") as f:
            source = f.read()
        self.assertNotIn("elif", source)
        self.assertNotIn("discount_type", source)

    def test_two_orders_can_share_one_strategy(self):
        shared = PercentageDiscount(10)
        a, b = make_order_total_250(shared), make_order_total_250(shared)
        self.assertAlmostEqual(a.calculate_total(), b.calculate_total())


class TestProductFactory(unittest.TestCase):
    def test_creates_physical(self):
        p = ProductFactory.create("physical", "1", "Lamp", 10.0, 5, make_supplier())
        self.assertIsInstance(p, PhysicalProduct)
        self.assertIsInstance(p, Product)

    def test_creates_digital(self):
        p = ProductFactory.create("digital", "2", "eBook", 10.0, 5, make_supplier())
        self.assertIsInstance(p, DigitalProduct)

    def test_unknown_type_raises_value_error_with_message(self):
        with self.assertRaises(ValueError) as ctx:
            ProductFactory.create("service", "3", "Install", 10.0, 5, make_supplier())
        self.assertIn("Unknown product type: service", str(ctx.exception))


class TestValidation(unittest.TestCase):
    def test_price_must_be_positive(self):
        for bad in (0, -1):
            with self.assertRaises(ValueError):
                ProductFactory.create("physical", "1", "X", bad, 1, make_supplier())

    def test_stock_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("digital", "1", "X", 5.0, -1, make_supplier())

    def test_zero_stock_is_allowed(self):
        self.assertEqual(ProductFactory.create("digital", "1", "X", 5.0, 0, make_supplier()).get_stock(), 0)

    def test_update_stock_rejects_negative_for_every_subclass(self):
        for product_type in ("physical", "digital"):
            p = ProductFactory.create(product_type, "1", "X", 5.0, 3, make_supplier())
            with self.assertRaises(ValueError):
                p.update_stock(-5)
            self.assertEqual(p.get_stock(), 3)  # unchanged after the failure

    def test_order_line_quantity_must_be_positive(self):
        p = ProductFactory.create("physical", "1", "X", 5.0, 3, make_supplier())
        for bad in (0, -2):
            with self.assertRaises(ValueError):
                OrderLine(p, bad)

    def test_order_rejects_bad_quantity_and_adds_no_line(self):
        order = Order("ORD001")
        p = ProductFactory.create("physical", "1", "X", 5.0, 3, make_supplier())
        with self.assertRaises(ValueError):
            order.add_order_line(p, 0)
        self.assertEqual(order.get_order_lines(), [])


class TestGetPositiveFloat(unittest.TestCase):
    def test_reprompts_until_valid(self):
        buffer = io.StringIO()
        with patch("builtins.input", side_effect=["abc", "-5", "12.50"]), redirect_stdout(buffer):
            result = get_positive_float("Price: ")
        self.assertEqual(result, 12.50)
        output = buffer.getvalue()
        self.assertIn("Please enter a valid number", output)
        self.assertIn("greater than zero", output)

    def test_zero_is_rejected(self):
        with patch("builtins.input", side_effect=["0", "3"]), redirect_stdout(io.StringIO()):
            self.assertEqual(get_positive_float("Price: "), 3.0)


class TestLoadProducts(unittest.TestCase):
    def test_missing_file_is_handled(self):
        inventory, buffer = Inventory(), io.StringIO()
        with redirect_stdout(buffer):
            load_products("does_not_exist.csv", inventory, make_supplier())  # must not raise
        output = buffer.getvalue()
        self.assertIn("Products file not found", output)
        self.assertIn("Load attempt finished.", output)
        self.assertNotIn("products loaded", output)  # else block did not run
        self.assertEqual(inventory.products, [])

    def test_bad_rows_skipped_and_valid_rows_load(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "products.csv")
            with open(path, "w", newline="") as f:
                f.write(CSV_TEXT)
            inventory, buffer = Inventory(), io.StringIO()
            with redirect_stdout(buffer):
                load_products(path, inventory, make_supplier())
        output = buffer.getvalue()
        self.assertEqual([p.get_product_id() for p in inventory.products], ["P001", "D001", "P003"])
        self.assertIn("Unknown product type: service", output)
        self.assertIn("3 products loaded.", output)
        self.assertTrue(output.rstrip().endswith("Load attempt finished."))


if __name__ == "__main__":
    unittest.main()
