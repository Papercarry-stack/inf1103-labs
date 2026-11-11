from abc import ABC, abstractmethod
from Supplier import Supplier


class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier):
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        # Association: Product keeps a reference to a Supplier it did not create.
        self.__supplier: Supplier = supplier

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def update_stock(self, new_stock: int) -> None:
        """Set the stock level. Every Product (and subclass) must support this."""
        self.__stock = new_stock

    def display_information(self) -> str:
        return (f"{self.__product_id} | {self.__name} | ${self.__price:.2f} | "
                f"stock: {self.__stock} | supplier: {self.__supplier.get_name()}")

    def to_dict(self) -> dict:
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict(),
        }

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
