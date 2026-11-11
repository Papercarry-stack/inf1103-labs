from Product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size

    def get_fulfilment_info(self):
        return "Delivered digitally via download link"

    def display_information(self):
        show_product = super().display_information()
        show_product += " | size: " + str(self.__download_size) + "MB"
        show_product += " | " + self.get_fulfilment_info() + "\n"
        return show_product