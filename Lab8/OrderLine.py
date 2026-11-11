from Product import Product


class OrderLine:
    """One product + quantity inside ONE order.

    Composition: an OrderLine is created by, belongs to, and is managed by an
    Order. Do not create OrderLine objects outside Order.add_order_line().
    It refers to a Product but does not own it.
    """

    def __init__(self, product: Product, quantity: int):
        self.__product: Product = product
        self.__quantity: int = quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def display_information(self) -> str:
        return (f"{self.__product.get_name()} x{self.__quantity} "
                f"@ ${self.__product.get_price():.2f} = "
                f"${self.calculate_subtotal():.2f}")
