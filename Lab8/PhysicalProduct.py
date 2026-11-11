from Product import Product
from CanBeShipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def get_fulfilment_info(self):
        return "Requires physical shipping"

    def calculate_shipping_cost(self):
        return float(self.__weight) * 2.50

    def display_information(self):
        show_product = super().display_information()
        show_product += " | weight: " + str(self.__weight) + "kg"
        show_product += " | " + self.get_fulfilment_info()
        show_product += " | shipping: $" + f"{self.calculate_shipping_cost():.2f}" + "\n"
        return show_product