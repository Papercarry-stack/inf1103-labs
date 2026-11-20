from BulkDiscount import BulkDiscount
from DiscountStrategy import DiscountStrategy
from helpers import get_positive_float, load_products
from Inventory import Inventory
from NoDiscount import NoDiscount
from Order import Order
from PercentageDiscount import PercentageDiscount
from Product import Product
from ProductFactory import ProductFactory
from StudentDiscount import StudentDiscount
from Supplier import Supplier


def read_int(prompt: str) -> int:
    """Keep asking until the input is a whole number."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid number, please try again.")


def next_supplier_id(suppliers: list[Supplier]) -> str:
    numbers = [int(s.get_supplier_id()[1:]) for s in suppliers]
    return f"S{max(numbers, default=0) + 1:03d}"


def choose_supplier(inventory: Inventory) -> Supplier:
    suppliers = inventory.get_suppliers()
    if suppliers:
        print("Existing suppliers:")
        for supplier in suppliers:
            print("  " + supplier.display_information())
        chosen_id = input("Enter Supplier ID to reuse (or press Enter for new): ")
        for supplier in suppliers:
            if supplier.get_supplier_id() == chosen_id:
                return supplier
    # The Supplier is created independently, then handed to the Product.
    name = input("Supplier Name: ")
    email = input("Supplier Contact Email: ")
    return Supplier(next_supplier_id(suppliers), name, email)


def choose_discount() -> DiscountStrategy:
    """Map a menu choice to a strategy. Order itself never sees these choices."""
    options = {
        "1": NoDiscount(),
        "2": PercentageDiscount(10),
        "3": BulkDiscount(200, 20),
        "4": StudentDiscount(),
    }
    print("Discount: 1. None  2. 10% off  3. 20 off totals of 200+  4. Student 5%")
    choice = input("Choose discount (default 1): ")
    return options.get(choice, NoDiscount())


def create_order(inventory: Inventory, order_number: int) -> Order:
    order = Order(f"ORD{order_number:03d}", choose_discount())
    while True:
        product_id = input("Product ID to add (press Enter to finish): ")
        if product_id == "":
            break
        product = inventory.find_product(product_id)
        if product is None:
            print("Product not found.")
            continue
        quantity = read_int("Quantity: ")
        try:
            order.add_order_line(product, quantity)
        except ValueError as error:
            print(error)
    return order


def main() -> None:
    inventory = Inventory()
    inventory.load_inventory()
    orders: list[Order] = []

    while True:
        print("----------MENU----------\n"
              "1. Display All Products\n"
              "2. Add Product\n"
              "3. Update Stock\n"
              "4. Search Product\n"
              "5. Remove Product\n"
              "6. Create Order\n"
              "7. Save Inventory\n"
              "8. Load Products from CSV\n"
              "9. Exit\n"
              "-------------------------")
        choice = input("Enter Option: ")

        match choice:
            case "1":
                print(inventory.display_all())
            case "2":
                next_id = inventory.generate_next_id()
                print(f"Product ID : {next_id}")
                type_choice = input("Enter product type (1: Physical, 2: Digital): ")
                while type_choice not in ["1", "2"]:
                    print("Invalid choice. Please enter either 1 or 2.")
                    type_choice = input("Product Type (1: Physical, 2: Digital): ")
                name = input("Product Name: ")
                price = get_positive_float("Price: ")
                stock = read_int("Stock Quantity: ")
                supplier = choose_supplier(inventory)
                if type_choice == "1":
                    product_type = "physical"
                    attribute = get_positive_float("Weight (kg): ")
                else:
                    product_type = "digital"
                    attribute = get_positive_float("Download Size (MB): ")
                try:
                    new_product: Product = ProductFactory.create(
                        product_type, next_id, name, price, stock, supplier, attribute)
                except ValueError as error:
                    print(f"Could not add product: {error}")
                else:
                    inventory.add_product(new_product)
                    print("Product added successfully!")
            case "3":
                product = inventory.find_product(input("Enter Product ID: "))
                if product is None:
                    print("Product not found.")
                else:
                    try:
                        product.update_stock(read_int("New Stock Quantity: "))
                        print("Stock updated successfully!")
                    except ValueError as error:
                        print(f"Stock not updated: {error}")
            case "4":
                product = inventory.find_product(input("Enter Product ID to search: "))
                if product is None:
                    print("Product not found.")
                else:
                    print("Product Found\n" + product.display_information())
                    print(product.get_supplier().display_information())
            case "5":
                removed = inventory.remove_product(input("Enter Product ID to remove: "))
                if removed is None:
                    print("Product not found.")
                else:
                    print(f"Removed '{removed.get_name()}' from inventory "
                          "(the product object itself still exists).")
            case "6":
                order = create_order(inventory, len(orders) + 1)
                orders.append(order)
                print(order.display_information())
            case "7":
                inventory.save_inventory()
                print("Inventory successfully saved to inventory.json")
            case "8":
                path = input("CSV file path (default products.csv): ") or "products.csv"
                load_products(path, inventory, choose_supplier(inventory))
            case "9":
                inventory.save_inventory()
                print("Inventory saved successfully.")
                print("Thank you for using Inventory Management System.\nProgram terminated..")
                break
            case _:
                print("Invalid option. Please choose between 1 and 9.")


if __name__ == "__main__":
    main()
