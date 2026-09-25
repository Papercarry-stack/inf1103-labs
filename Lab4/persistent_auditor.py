#1. Initialize the inventory to zero in the start
#2. Run in a continuous loop asking user to enter a stock quantity, until the user
#types quit. (Think of which loop might be helpful here: for or while)
#3. Accept stock values as integers.
#4. Handle invalid input: If the user enters a string (e.g., "ten"), reject it, print an
#error, and move to the next iteration. (Hint: use.isdigit()).
#5. Enforce business rules: Reject negative numbers.
#6. Manage State: Keep a running total of the inventory.
#7. Trigger Overstock Alert: If the total inventory exceeds 500 units, print an
#alert and break the loop immediately. (keep in mind of the conditional flow we
#discussed this week: if, elif and else)
#8. Reporting: When the user types quit, print the Total Units Processed and the
#Number of Failed/Rejected Entries.

import csv

MAX_INVENTORY = 500
TAX = 0.1

def process_delivery(current_total, new_value):
    total = current_total + new_value
    return(total)

def calculate_tax(amount):
    tax_amount = amount * TAX 
    return(tax_amount)

def generate_report(total_units, failed_attempts):
    print (f"Total inventory: {total_units}\nFailed Attemps: {failed_attempts}" )

def get_valid_input():
    
    product = input("Enter Product Name: ")
    quantity = input("Enter Quantity: ")
    new_order = [product, quantity]
    return(new_order)

def load_inventory():
    # Open the file in read mode
    inventory = []
    with open("Lab4/inventory.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Skip empty rows
                # Convert ID and quantity back to integers, and keep the name as a string
                item_id = int(row[0])
                name = row[1].strip()
                quantity = int(row[2])
                inventory.append([item_id, name, quantity])
    return (inventory)

def veiw_order(inventory):
    o = 0
    show_inv = ""
    i=len(inventory)
    while o < i:
        show_inv += str(inventory[o][0]) + ", "
        show_inv += str(inventory[o][1]) + ", "
        show_inv += str(inventory[o][2]) + "\n"
        o += 1
    return(show_inv)

def get_neworder(inventory):
    new_order = get_valid_input()
    count = inventory[-1][0] + 1
    new_order.insert(0,count)
    #print(new_order)
    print("\nNew Order Added:\n" + str(new_order[0]) + ", " + str(new_order[1]) + ", " + str(new_order[2]) + "\n")
    inventory.append(new_order)

    return inventory

def totally_get_neworder():
    print("No Current Orders\n")
    inventory = []
    new_order = get_valid_input()
    count = 1
    new_order.insert(0,count)
    print(new_order)
    print("New Order Added:\n" + str(new_order[0]) + ", " + str(new_order[1]) + ", " + str(new_order[2]) + "\n")
    inventory.append(new_order)
    return inventory

def save_inventory(inventory):
    with open("Lab4/inventory.txt", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(inventory)
    print ("Order successfully saved to inventory.txt")

def main():
    
    try:
        inventory = load_inventory()
        print("Current Orders : \n" + veiw_order(inventory) + "\n")
        get_neworder(inventory)
        save_inventory(inventory)
    except FileNotFoundError:
        with open('Lab4/inventory.txt', 'w') as file:
            inventory = totally_get_neworder()
            save_inventory(inventory)
    

#    print(veiw_order(new_inventory))

if __name__=="__main__":
    main()

