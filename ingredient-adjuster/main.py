#
# Jordan Williford
# 1/17/2025
# Ingredient Adjuster Programming Project
# SDEV 1200 
#

# Declare variables.
sugar = float(1.5)
butter = float(1)
flour =float(2.75)
cookies =float(48)
# Use comments liberally throughout the program.
def main():
    number_of_cookies= input("How many cookies would you like to make?")
    number_of_cookies = float(number_of_cookies)
#These next 3 lines will calculate the amount of each ingredient for the user based on their input
    total_sugar= (sugar*number_of_cookies) / cookies
    total_butter= (butter*number_of_cookies) / cookies
    total_flour= (flour*number_of_cookies) / cookies
    rounded_sugar=round(total_sugar,2)
    rounded_butter=round(total_butter,2)
    rounded_flour=round(total_flour,2)
#This will display what the user will need for the desired number of cookies
    print("You will need", rounded_sugar,"cups sugar")
    print("You will need", rounded_butter, "cups butter")
    print("You will need",rounded_flour,"cups flour")
main()