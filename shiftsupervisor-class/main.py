#
# Jordan Williford
# 3/2/2025
# ShiftSupervisor Class Programming Project
# SDEV 1200
#
#Use comments liberally throughout the program.
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def get_name(self):
        return self.name

    def get_employee_id(self):
        return self.employee_id

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def __str__(self):
        return f"Employee Name: {self.name}\nEmployee ID: {self.employee_id}\nSalary: ${self.salary:.2f}"

class ShiftSupervisor(Employee):
    def __init__(self, name, employee_id, salary, annual_bonus):
        # Call the superclass constructor to initialize name, employee_id, and salary
        super().__init__(name, employee_id, salary)
        self.annual_bonus = annual_bonus

    def get_annual_bonus(self):
        return self.annual_bonus

    def set_annual_bonus(self, bonus):
        self.annual_bonus = bonus

    def total_compensation(self):
        return self.salary + self.annual_bonus

    def __str__(self):
        # Override __str__ to include bonus and total compensation
        return (f"{super().__str__()}\nAnnual Bonus: ${self.annual_bonus:.2f}\n"
                f"Total Compensation: ${self.total_compensation():.2f}")

def main():
    # Gather user input for the ShiftSupervisor details
    print("Enter the details of the Shift Supervisor:")

    name = input("Enter the name of the supervisor: ")
    employee_id = int(input("Enter the employee ID: "))
    salary = float(input("Enter the annual salary of the supervisor: "))
    annual_bonus = float(input("Enter the annual production bonus of the supervisor: "))

    # Create a ShiftSupervisor object using the input data
    supervisor = ShiftSupervisor(name, employee_id, salary, annual_bonus)

    # Display the details of the supervisor
    print("\nShift Supervisor Details:")
    print(supervisor)

if __name__ == "__main__":
    main()
