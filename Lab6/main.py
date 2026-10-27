import json
import os
from Product import Product 
from Inventory import Inventory


def main():  
       inventory = Inventory()
       print("----------MENU----------\n" \
       "1. Display All Products\n" \
       "2. Add Product\n" \
       "3. Update Stock\n" \
       "4. Search Product\n" \
       "5. Save Inventory\n" \
       "6. Exit\n" \
       "-------------------------" )
       i = input("Enter Option: ")
       while True :
            match i:
                case "1":
                    inventory.display_all()
                case "2":
                    next_id = inventory.generate_next_id()
                    print(f"Product ID : {next_id}")
                    name = input("Product Name: ")
                    price = f"{float(input('Price: ')):.2f}"
                    stock = input("Stock Quantity: ")
                    new_product = Product(next_id, name, price, stock)
                    inventory.add_product(new_product)
                case "3":
                    id_tofind = input("Enter Product ID to search: ")
                    found_product = inventory.search_product(id_tofind)
                    if found_product == None:
                        continue
                    else:
                        new_stock =  input("New Stock Quantity:")
                        found_product.update_stock(new_stock)
                        print("Stock updated successfully!")
                case "4":
                   id_tofind = input("Enter Product ID to search: ")
                   inventory.search_product(id_tofind)
                # case "5":
                #    print("Saving inventory...")
                #    save_inventory(inventory)
                #    print ("Order successfully saved to inventory.txt")
                # case "6":
                #    print("Saving inventory before exit...")
                #    save_inventory(inventory)
                #    print("Inventory saved successfully.")
                #    print("Thank you for using Inventory Management System.\nProgram terminated..")
                #    break
                case _:
                   print("Invalid option. Please choose between 1 and 6.")
            i = input("Enter Option: ")

if __name__ == "__main__":
    main()