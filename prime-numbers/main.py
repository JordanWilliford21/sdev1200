#
# Jordan Williford
# 2/25/2025
# Prime Number Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 
def is_prime(num):
    """
    Checks if a given number is prime.
    
    Args:
        num: The integer to check for primality.
    
    Returns:
        True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Get user input
number = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")