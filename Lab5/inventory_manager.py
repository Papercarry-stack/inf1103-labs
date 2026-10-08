import json
import os


def load_inventory():
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


def save_inventory(inventory):

    with open("inventory.json","w") as f:
        json.dump(inventory, f, indent=4)
        json.dumps


def display_all(inventory):
    show_inv = ""
    for product in inventory:
        show_inv += str(product["ID"]) + " | "
        show_inv += str(product["Name"]) + " | "
        show_inv += "$" + str(product["Price"]) + " | "
        show_inv += "stock: " + str(product["Stock"]) + "\n"
    print("Displaying all products...")
    print(
        "Current Inventory\n" \
        "-----------------------------------------\n" \
        + show_inv \
        + "-----------------------------------------")


def add_product(inventory):
    print("Add New Product")
    if len(inventory) == 0:
        next_id = "001"
    else:
        last_id = inventory[-1]["ID"]
        next_id = f"{int(last_id) + 1:03d}"
    print(f"Product ID : {next_id}")
    name = input("Product Name: ")
    price = f"{float(input('Price: ')):.2f}"
    stock = input("Stock Quantity: ")
    new_product = {
        "ID": next_id,
        "Name": name,
        "Price": price,
        "Stock": stock
    }
    inventory.append(new_product)
    print("Product added successfully!\n")


def update_stock(inventory):
    id_tofind= input("Enter ID to update: ")
    found_product = None
    show_pro ="Product Found: \n"
    for product in inventory:
        if product["ID"] == id_tofind:
            found_product = product
            show_pro += "\nName: " + str(product["Name"]) + " \n"
            show_pro += "stock: " + str(product["Stock"]) + "\n"
            print(show_pro)
            break
    if found_product:
        new_stock = input("New Stock Quantity: ")
        found_product["Stock"] = new_stock
        print("Stock updated successfully!")
    else:
        print("Product not found \n")


def search_product(inventory):
    id_tofind = input("Enter Product ID to search: ")
    show_pro = ""
    found_product = None
    for product in inventory:
            if product["ID"] == id_tofind:
                found_product = product
                break
    if found_product:
        print("Product Found \n--------------------------------------")
        show_pro += "\nID: " + str(found_product["ID"]) + " \n"
        show_pro += "Name: " + str(found_product["Name"]) + " \n"
        show_pro += "Price: " + str(found_product["Price"]) + " \n"
        show_pro += "stock: " + str(found_product["Stock"]) + "\n"
        print(show_pro)
        print("--------------------------------------")
    else:
        print("Product not found \n")

def main():  
    inventory = load_inventory()
    print("----------MENU----------\n" \
    "1. Display All Products\n" \
    "2. Add Product\n" \
    "3. Update Stock\n" \
    "4. Search Product\n" \
    "5. Save Inventory\n" \
    "6. Exit\n" \
    "-------------------------" )
    i = int(input("Enter Option: "))
    while True :
        match i:
            case 1:
                display_all(inventory)
            case 2:
                add_product(inventory)
            case 3:
                update_stock(inventory)
            case 4:
                search_product(inventory)
            case 5:
                print("Saving inventory...")
                save_inventory(inventory)
                print ("Order successfully saved to inventory.txt")
            case 6:
                print("Saving inventory before exit...")
                save_inventory(inventory)
                print("Inventory saved successfully.")
                print("Thank you for using Inventory Management System.\nProgram terminated..")
                break
            case _:
                print("Invalid option. Please choose between 1 and 6.")
        i = int(input("Enter Option: "))



    

#    print(veiw_order(new_inventory))

if __name__=="__main__":
    main()



