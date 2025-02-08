#
# Jordan Williford
# 2/7/2025
# RetailItem Class Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program. 
class RetailItem:
    def __init__(self, description, units_in_inventory, price):
        self.description = description
        self.units_in_inventory = units_in_inventory
        self.price = price 

# Create three RetailItem objects
item1 = RetailItem("Jacket", 12, 59.95)
item2 = RetailItem("Designer Jeans", 40, 34.95)
item3 = RetailItem("Shirt", 20, 24.95) 

# Print details of each item
print("Item 1:")
print(f"Description: {item1.description}, Units in Inventory: {item1.units_in_inventory}, Price: {item1.price}")

print("\nItem 2:")
print(f"Description: {item2.description}, Units in Inventory: {item2.units_in_inventory}, Price: {item2.price}")

print("\nItem 3:")
print(f"Description: {item3.description}, Units in Inventory: {item3.units_in_inventory}, Price: {item3.price}")