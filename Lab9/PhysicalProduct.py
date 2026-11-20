from Product import Product
from CanBeShipped import CanBeShipped
from Supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 weight: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight

    def get_weight(self) -> float:
        return self.__weight

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping"

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 2.50

    def display_information(self) -> str:
        return (super().display_information()
                + f" | weight: {self.__weight}kg"
                + f" | {self.get_fulfilment_info()}"
                + f" | shipping: ${self.calculate_shipping_cost():.2f}")

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data
