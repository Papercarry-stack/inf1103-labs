import json
import os
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Inventory import Inventory

def main():  
    inventory = Inventory()
    while True:
        print("----------MENU----------\n" \
              "1. Display All Products\n" \
              "2. Add Product\n" \
              "3. Update Stock\n" \
              "4. Search Product\n" \
              "5. Save Inventory\n" \
              "6. Exit\n" \
              "-------------------------")
        i = input("Enter Option: ")
        
        match i:
            case "1":
                inventory.display_all()
            case "2":
                next_id = inventory.generate_next_id()
                print(f"Product ID : {next_id}")
                
                type_choice = input("Enter product type (1: Physical, 2: Digital): ")
                while type_choice not in ["1", "2"]:
                    print("Invalid choice. Please enter either 1 or 2.")
                    type_choice = input("Product Type (1: Physical, 2: Digital): ")
                name = input("Product Name: ")
                price = f"{float(input('Price: ')):.2f}"
                stock = input("Stock Quantity: ")
                if type_choice == "1":
                    weight = input("Weight (kg): ")
                    new_product = PhysicalProduct(next_id, name, price, stock, weight)
                elif type_choice == "2":
                    download_size = input("Download Size (MB): ")
                    new_product = DigitalProduct(next_id, name, price, stock, download_size)
                else:
                    print("Enter either 1 or 2")
                    
                inventory.add_product(new_product)
            case "3":
                id_tofind = input("Enter Product ID to search: ")
                found_product = inventory.search_product(id_tofind)
                if found_product is not None:
                    new_stock = input("New Stock Quantity: ")
                    found_product.update_stock(new_stock)
                    print("Stock updated successfully!")
            case "4":
                id_tofind = input("Enter Product ID to search: ")
                inventory.search_product(id_tofind)
            case "5":
                print("Saving inventory...")
                inventory.save_inventory()
                print("Inventory successfully saved to inventory.json")
            case "6":
                print("Saving inventory before exit...")
                inventory.save_inventory()
                print("Inventory saved successfully.")
                print("Thank you for using Inventory Management System.\nProgram terminated..")
                break
            case _:
                print("Invalid option. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()