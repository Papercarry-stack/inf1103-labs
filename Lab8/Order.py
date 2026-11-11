from OrderLine import OrderLine
from Product import Product


class Order:
    def __init__(self, order_id: str):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def get_order_id(self) -> str:
        return self.__order_id

    def get_order_lines(self) -> list[OrderLine]:
        # Return a copy so outside code cannot add/remove lines behind Order's back.
        return list(self.__order_lines)

    def add_order_line(self, product: Product, quantity: int) -> None:
        # Order creates its own OrderLine (composition).
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> bool:
        """Remove the line for product_id. Returns True if a line was removed."""
        for order_line in self.__order_lines:
            if order_line.get_product().get_product_id() == product_id:
                self.__order_lines.remove(order_line)
                return True
        return False

    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()
        return total

    def display_information(self) -> str:
        lines = [f"Order {self.__order_id}"]
        for order_line in self.__order_lines:
            lines.append("  " + order_line.display_information())
        lines.append(f"  Total: ${self.calculate_total():.2f}")
        return "\n".join(lines)
