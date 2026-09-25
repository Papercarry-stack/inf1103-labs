import csv

inventory = []

# Open the file in read mode
with open("Lab4/inventory.txt", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row:  # Skip empty rows
            # Convert ID and quantity back to integers, and keep the name as a string
            item_id = int(row[0])
            name = row[1].strip()
            quantity = int(row[2])
            
            inventory.append([item_id, name, quantity])

print(inventory)

