#
# Jordan Williford
# 1/24/2025
# Pennies for Pay Programming Project
# SDEV 1200 
#

# Use comments liberally throughout the program.
def calculate_pennies(num_days):
    total = 0
    for day in range(1, num_days + 1):
        salary = 2 ** (day - 1) * 0.01  # Calculate daily salary
        total += salary
    return total
def main(): # this will get ask the user for number of days
    num_days = int(input("Enter the number of days: "))
    print("Day\tSalary")
    print("----\t-----")
    for day in range(1, num_days + 1): # this will calculate the pennies and display them as a dollar amount
        salary = 2 ** (day - 1) * 0.01
        print(day, "\t$", format(salary, ".2f"))
    total_pay = calculate_pennies(num_days)
    print("\nTotal Pay: $", format(total_pay, ".2f"))

if __name__ == "__main__":
    main()