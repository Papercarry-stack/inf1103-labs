class Product():
    def __init__(self,product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    def update_stock(self, new_stock):
        self._stock = new_stock

    def display_information(self):
        show_product = ""
        show_product += str(self._product_id) + " | "
        show_product += str(self._name) + " | "
        show_product += "$" + str(self._price) + " | "
        show_product += "stock: " + str(self._stock) + "\n"
        return show_product
