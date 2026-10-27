import json
import os

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
            inventory = json.load(file)
            
        return inventory

my_inventory = Inventory()
print(my_inventory.inventory)