class Product():
    def __init__(self,product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        product_id = self.__product_id
        return product_id

    def get_name(self):
        name = self.__name
        return name

    def get_price(self):
        price = self.__price
        return price

    def get_stock(self):
        stock = self.__stock
        return stock

    def update_stock(self, new_stock):
        self.__stock = new_stock

    def display_information(self):
        show_product = ""
        show_product += str(self.__product_id) + " | "
        show_product += str(self.__name) + " | "
        show_product += "$" + str(self.__price) + " | "
        show_product += "stock: " + str(self.__stock) + "\n"
        return show_product
