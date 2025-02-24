#
# Jordan Williford
# 2/2
# Person and Customer Classes Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.

import person

# Main function to demonstrate creating and using an instance of the Customer class
def main():
    # Get input data for a customer.
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    telephone = input("Enter your telephone number: ")
    customer_number = input("Enter your customer number: ")
    on_mailing_list = input("Do you wish to be on the mailing list? (yes/no): ").strip().lower()

    # Convert 'yes'/'no' to Boolean
    on_mailing_list = on_mailing_list == 'yes'

    # Create an instance of the Customer class
    customer = person.Customer(name, address, telephone, customer_number, on_mailing_list)

    # Display the customer's information
    print("\nCustomer Information:")
    print(f"Name: {customer.name}")
    print(f"Address: {customer.address}")
    print(f"Telephone: {customer.telephone}")
    print(f"Customer Number: {customer.customer_number}")
    print(f"On Mailing List: {'Yes' if customer.on_mailing_list else 'No'}")

# Run the main function
if __name__ == "__main__":
    main()

