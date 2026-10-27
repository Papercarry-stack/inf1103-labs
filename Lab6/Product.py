class Product():
    def __init__(self,product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, new_stock):
        self.__stock = new_stock

    def display_information(self):
        show_product = ""
        show_product += str(self.__product_id) + " | "
        show_product += str(self.__name) + " | "
        show_product += "$" + str(self.__price) + " | "
        show_product += "stock: " + str(self.__stock) + "\n"
        return show_product

product1 = Product("001", "mouse", 10,50)
product2 = Product("001", "keyboard", 20,10)

print(product1, product2)

product2.update_stock(30)

# print(product2.__dict__)

print(product2.display_information())