#
# Jordan Williford
# 2/15/2025
# Cash Register Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 
class RetailItem:
    def __init__(self, description, price):
        self.description = description
        self.price = price 

    def get_price(self):
        return self.price 

class CashRegister:
    def __init__(self):
        self.cart = [] 

    def add_item(self, item):
        self.cart.append(item)

    def get_total(self):
        total = 0
        for item in self.cart:
            total += item.get_price()
        return total 

    def display_cart(self):
        print("Your cart:")
        for item in self.cart:
            print(f"- {item.description}: ${item.price:.2f}") 
        print(f"Total: ${self.get_total():.2f}") 

# Example usage 
if __name__ == "__main__":
    register = CashRegister()
    
    register.add_item(RetailItem("Apple", 0.50))
    register.add_item(RetailItem("Banana", 0.30))
    register.add_item(RetailItem("Orange", 0.60)) 

    register.display_cart()