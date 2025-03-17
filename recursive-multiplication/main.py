#
# Jordan Williford
# 3/16/2025
# Recursive Multiplication Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program. 
def recursive_multiply(x, y):
    # Base case: If y is 1, return x
    if y == 1:
        return x
    # Recursive case: Add x to the result of multiplying x and (y-1)
    else:
        return x + recursive_multiply(x, y - 1)

# Example usage:
result = recursive_multiply(7, 4)
print(result)  # Output will be 28
