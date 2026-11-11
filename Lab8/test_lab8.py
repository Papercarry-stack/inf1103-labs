"""Lab 8 demonstration tests. Run: python test_lab8.py"""
from DigitalProduct import DigitalProduct
from Inventory import Inventory
from Order import Order
from PhysicalProduct import PhysicalProduct
from Product import Product
from Supplier import Supplier


def show_product_details(product: Product) -> None:
    """Works for ANY Product - no isinstance needed (LSP + polymorphism)."""
    print(product.display_information())
    print(product.get_fulfilment_info())


def section(title: str) -> None:
    print(f"\n===== {title} =====")


# ---------- Section 2: association ----------
section("2. Association: Supplier and Product")
supplier = Supplier("S001", "TechSource", "sales@techsource.com")
laptop = PhysicalProduct("001", "Laptop", 1200.0, 15, 2.2, supplier)
ebook = DigitalProduct("002", "Python eBook", 19.99, 100, 5.5, supplier)
print(laptop.get_supplier().display_information())
print(ebook.get_supplier().display_information())
assert laptop.get_supplier() is supplier and ebook.get_supplier() is supplier

del supplier  # removes the NAME only; the objects still reference the Supplier
print("After del supplier ->", laptop.get_supplier().display_information())
assert laptop.get_supplier().get_name() == "TechSource"

# ---------- Section 3: aggregation ----------
section("3. Aggregation: Inventory and Product")
mouse = PhysicalProduct("003", "Mouse", 40.0, 20, 0.1, laptop.get_supplier())
inv_a, inv_b = Inventory(), Inventory()
inv_a.add_product(mouse)
removed = inv_a.remove_product("003")
assert removed is mouse and inv_a.find_product("003") is None
print("Still usable after removal:", mouse.display_information())
inv_b.add_product(mouse)
assert inv_b.find_product("003") is mouse
inv_a.add_product(laptop)
inv_a.products.clear()  # emptying an inventory does not destroy products
print("Laptop after inventory emptied:", laptop.get_name(), laptop.get_stock())

# ---------- Section 4: composition ----------
section("4. Composition: Order and OrderLine")
order1, order2 = Order("ORD001"), Order("ORD002")
order1.add_order_line(laptop, 2)
order1.add_order_line(ebook, 3)
order2.add_order_line(laptop, 1)  # same Product, different Order
print(order1.display_information())
print(order2.display_information())
assert abs(order1.calculate_total() - (2 * 1200.0 + 3 * 19.99)) < 1e-9
line1 = order1.get_order_lines()[0]
line2 = order2.get_order_lines()[0]
assert line1 is not line2                         # 2 separate OrderLines
assert line1.get_product() is line2.get_product() # 1 shared Product
print("Two OrderLines, one Product:", id(line1) != id(line2),
      id(line1.get_product()) == id(line2.get_product()))
assert order1.remove_order_line("002") is True
assert len(order1.get_order_lines()) == 1
print("After removing a line:", order1.calculate_total())

# ---------- Section 6 and 7: LSP and polymorphism ----------
section("6. LSP: show_product_details with both subclasses")
show_product_details(laptop)
show_product_details(ebook)

section("7. Polymorphism: one loop, mixed Product types")
inventory = Inventory()
inventory.add_product(laptop)
inventory.add_product(ebook)
for product in inventory.products:
    print(product.display_information())
    print(product.get_fulfilment_info())

# LSP: update_stock behaves the same for every Product
for product in inventory.products:
    product.update_stock(7)
    assert product.get_stock() == 7
print("\nAll tests passed.")
