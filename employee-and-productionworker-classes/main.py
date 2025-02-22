#
# Jordan Williford
# 2/22/2025
# Employee And ProductionWorker Classes Programming Project
# SDEV 1200
#

# Use comments liberally through the program.
# Employee class definition
# Employee class definition
class Employee:
    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = employee_number
    
    # Accessor methods
    def get_name(self):
        return self.name
    
    def get_employee_number(self):
        return self.employee_number
    
    # Mutator methods
    def set_name(self, name):
        self.name = name
    
    def set_employee_number(self, employee_number):
        self.employee_number = employee_number


# ProductionWorker class definition (inherits from Employee)
class ProductionWorker(Employee):
    def __init__(self, name, employee_number, shift_number, hourly_pay_rate):
        # Initialize attributes of the parent class (Employee)
        super().__init__(name, employee_number)
        # Initialize attributes specific to ProductionWorker
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate
    
    # Accessor methods
    def get_shift_number(self):
        return self.shift_number
    
    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate
    
    # Mutator methods
    def set_shift_number(self, shift_number):
        self.shift_number = shift_number
    
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.hourly_pay_rate = hourly_pay_rate
    
    # Method to get the shift description
    def get_shift_description(self):
        if self.shift_number == 1:
            return "Day Shift"
        elif self.shift_number == 2:
            return "Night Shift"
        else:
            return "Invalid Shift"


# Main program to interact with the user
if __name__ == "__main__":
    # Get employee details from the user
    name = input("Enter employee name: ")
    employee_number = input("Enter employee number: ")
    
    # Get production worker details from the user
    shift_number = int(input("Enter shift number (1 for Day, 2 for Night): "))
    hourly_pay_rate = float(input("Enter hourly pay rate: "))
    
    # Create an instance of ProductionWorker
    worker = ProductionWorker(name, employee_number, shift_number, hourly_pay_rate)
    
    # Display the information using accessor methods
    print("\nEmployee Information:")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_employee_number()}")
    print(f"Shift: {worker.get_shift_description()}")
    print(f"Hourly Pay Rate: ${worker.get_hourly_pay_rate():.2f}")
