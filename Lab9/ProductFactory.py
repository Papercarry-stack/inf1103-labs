from DigitalProduct import DigitalProduct
from PhysicalProduct import PhysicalProduct
from Product import Product
from Supplier import Supplier


class ProductFactory:
    """Centralises product creation. Callers only need to know Product and this class."""

    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock: int, supplier: Supplier, attribute: float = 1.0) -> Product:
        """attribute = weight (kg) for 'physical', download size (MB) for 'digital'."""
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock, attribute, supplier)
        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock, attribute, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")
