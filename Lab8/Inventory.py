import json
import os
from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier


class Inventory:
    """Aggregation: an Inventory holds references to Product objects but does
    not create them or control their lifecycle. Removing a product from an
    inventory does not destroy it."""

    def __init__(self, file_path: str = "inventory.json"):
        self.file_path: str = file_path
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product_id: str) -> Product | None:
        """Remove the reference and hand the Product back (it is NOT destroyed)."""
        product = self.find_product(product_id)
        if product is not None:
            self.products.remove(product)
        return product

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None

    def generate_next_id(self) -> str:
        numbers = [int(p.get_product_id()) for p in self.products]
        return f"{max(numbers, default=0) + 1:03d}"

    def get_suppliers(self) -> list[Supplier]:
        unique: dict[str, Supplier] = {}
        for product in self.products:
            supplier = product.get_supplier()
            unique.setdefault(supplier.get_supplier_id(), supplier)
        return list(unique.values())

    def display_all(self) -> str:
        lines = [product.display_information() for product in self.products]
        return ("Current Inventory\n"
                "-----------------------------------------\n"
                + "\n".join(lines)
                + "\n-----------------------------------------")

    def save_inventory(self) -> None:
        data = [product.to_dict() for product in self.products]
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def load_inventory(self) -> None:
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

        with open(self.file_path, "r") as f:
            all_items = json.load(f)

        suppliers: dict[str, Supplier] = {}
        loaded: list[Product] = []
        for item in all_items:
            supplier_data = item["supplier"]
            supplier_id = supplier_data["supplier_id"]
            if supplier_id not in suppliers:
                suppliers[supplier_id] = Supplier.from_dict(supplier_data)
            supplier = suppliers[supplier_id]

            if item.get("type") == "physical":
                product: Product = PhysicalProduct(
                    item["product_id"], item["name"], item["price"],
                    item["stock"], item["weight"], supplier)
            elif item.get("type") == "digital":
                product = DigitalProduct(
                    item["product_id"], item["name"], item["price"],
                    item["stock"], item["download_size"], supplier)
            else:
                continue
            loaded.append(product)
        self.products = loaded
