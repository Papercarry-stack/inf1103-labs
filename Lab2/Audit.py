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



inventory = 0

stock = input("Enter stock quantity (or type 'quit' to exit):")

while stock != "quit":
    if stock.isdigit() == True :
        inventory += int(stock)
        stock = input("Enter stock quantity (or type 'quit' to exit):")
    elif stock.isdigit() == False :
        print("invalid input please enter a number")
        stock = input("Enter stock quantity (or type 'quit' to exit):")

print("total inventry: " + str(inventory))

