#
# Jordan Williford
# 2/22/2015
# Person and Customer Classes Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.

class Person:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def display_info(self):
        return f"Name: {self.name}\nAddress: {self.address}\nPhone Number: {self.phone_number}"

# Customer class definition (inherits from Person)
class Customer(Person):
    def __init__(self, name, address, phone_number, customer_number, mailing_list):
        # Initialize attributes of the parent class
        super().__init__(name, address, phone_number)
        # Initialize additional attributes specific to Customer
        self.customer_number = customer_number
        self.mailing_list = mailing_list

    def display_customer_info(self):
        mailing_status = "Yes" if self.mailing_list else "No"
        return f"{self.display_info()}\nCustomer Number: {self.customer_number}\nMailing List: {mailing_status}"

