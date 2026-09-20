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



MAX_INVENTORY = 500
TAX = 0.1



def process_delivery(current_total, new_value):
    total = current_total + new_value
    return(total)

def calculate_tax(amount):
    tax_amount = amount * TAX 
    return(tax_amount)

def generate_report(total_units, failed_attempts):
    print ("Total inventory: " + total_units + "\nFailed Attemps: " + failed_attempts)

def get_valid_input(inventory, rejected):
    stock = input("Enter stock quantity (or type 'quit' to exit):")
    while stock.lower() != "quit":
        if stock.isdigit() == True :
            inventory += int(stock)
            if inventory > MAX_INVENTORY :
                print("Total Inventory exceeds 500 units.")
                break
            stock = input("Enter stock quantity (or type 'quit' to exit):")

        elif stock.isdigit() == False  : #isdigit also rejects -ve numbers
            print("invalid input please enter a positive number")
            stock = input("Enter stock quantity (or type 'quit' to exit):")
            rejected += 1
    return (inventory, rejected)

def main():
    inventory = 0
    rejected = 0
    inventory, rejected = get_valid_input(inventory, rejected)
    print(str(inventory) + " " + str(rejected))

if __name__=="__main__":
    main()

