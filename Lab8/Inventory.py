import json
import os
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

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
            # Check by unique attribute keys present in the dict
            if "_PhysicalProduct__weight" in item:
                product_obj = PhysicalProduct(
                    item["_Product__product_id"], 
                    item["_Product__name"], 
                    item["_Product__price"], 
                    item["_Product__stock"],
                    item["_PhysicalProduct__weight"]
                )
            elif "_DigitalProduct__download_size" in item:
                product_obj = DigitalProduct(
                    item["_Product__product_id"], 
                    item["_Product__name"], 
                    item["_Product__price"], 
                    item["_Product__stock"],
                    item["_DigitalProduct__download_size"]
                )
            else:
                continue
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
            last_id = self.inventory[-1].get_product_id() 
            return f"{int(last_id) + 1:03d}"

    def search_product(self, id_tofind):
        show_pro = ""
        found_product = None
        for product in self.inventory:
                product_id = product.get_product_id()
                if product_id == id_tofind:
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