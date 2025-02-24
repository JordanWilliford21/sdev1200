#
# Jordan Williford
# 2/22/2015
# Person and Customer Classes Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.
# Define the Person class with data attributes.
class Person:
    def __init__(self, name, address, telephone):
        # Initialize the Person class attributes
        self.name = name
        self.address = address
        self.telephone = telephone

# Define the Customer class, which is a subclass of Person
class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, on_mailing_list):
        # Call the parent constructor to initialize Person attributes
        super().__init__(name, address, telephone)
        # Initialize additional attributes for the Customer class
        self.customer_number = customer_number
        self.on_mailing_list = on_mailing_list
