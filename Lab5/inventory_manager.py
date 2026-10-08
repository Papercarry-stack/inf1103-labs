import json


def load_inventory():
# Open the JSON file in read mode
    with open("inventory.json", "r") as file:
        inventory = json.load(file)        
    return inventory


def save_inventory(inventory):
    with open("inventory.json","w") as f:
        json.dump(inventory, f, indent=4)
        json.dumps
    print ("Order successfully saved to inventory.txt")


def menu():
    print("----------MENU----------\n" \
    "1. Display All Products\n" \
    "2. Add Product\n" \
    "3. Update Stock\n" \
    "4. Search Product\n" \
    "5. Save Inventory\n" \
    "6. Exit\n" \
    "-------------------------" )
    i = int(input("Enter Option: "))
    while i != 6 :
        match i:
            case 1:
                print("Displaying all products...")

            case 2:
                print("Adding a product...")
            # call your add function here
            case 3:
                print("Updating stock...")
            # call your update function here
            case 4:
                print("Searching for a product...")
            # call your search function here
            case 5:
                print("Saving inventory...")
            # call your save function here
            case _:
                print("Invalid option. Please choose between 1 and 6.")
        i = int(input("Enter Option: "))

    
    

def main():  
    inventory = load_inventory()
    print(inventory)
    menu()


    

#    print(veiw_order(new_inventory))

if __name__=="__main__":
    main()



