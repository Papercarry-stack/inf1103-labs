import json
import os
from Product import Product 

class Inventory():

    def __init__(self):
        self.inventory = self.load_inventory()

    def load_inventory(self):
        file_path = "inventory.json"
        
        # Check if the file exists before opening
        if not os.path.exists(file_path):
            # Create an empty file with an empty list structure
            with open(file_path, "w") as file:
                json.dump([], file)
                
        # Open and load the file normally
        with open(file_path, "r") as file:
            all_item = json.load(file)

        product_list = []
        for item in all_item:
            product_obj = Product(
                item["_product_id"], 
                item["_name"], 
                item["_price"], 
                item["_stock"]
            )
            product_list.append(product_obj)
        return product_list

    def display_all(self):
        show_inv = ""
        for product in self.inventory:
            show_inv += product.display_information()
        print("Displaying all products...")
        print(
            "Current Inventory\n" \
            "-----------------------------------------\n" \
            + show_inv \
            + "-----------------------------------------")

    def add_product(self, new_product):
        self.inventory.append(new_product)
        print("Product added successfully!\n")

    def generate_next_id(self):
        if len(self.inventory) == 0:
            return "001"
        else:
            last_id = self.inventory[-1]._product_id
            return f"{int(last_id) + 1:03d}"

    def search_product(self, id_tofind):
        show_pro = ""
        found_product = None
        for product in self.inventory:
                if product._product_id == id_tofind:
                    found_product = product
                    break
        if found_product:
            show_pro = ""
            show_pro += found_product.display_information()
            print("Product Found \n--------------------------------------")
            print(show_pro)
            print("--------------------------------------")
            return found_product
        else:
            print("Product not found \n")
            return found_product

    def save_inventory(self):
        savedata = []
        for product in self.inventory:
           savedata.append(product.__dict__)
        with open("inventory.json","w") as f:
            json.dump(savedata, f, indent=4)
            json.dumps