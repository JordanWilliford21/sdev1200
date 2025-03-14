#
# Jordan Williford
# 3/14/2025
# Ackermann's Function Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 
def ackermann(m, n):
    # Base case when m is 0
    if m == 0:
        return n + 1
    # Recursive case when n is 0
    elif n == 0:
        return ackermann(m - 1, 1)
    # Recursive case for m > 0 and n > 0
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# Test the Ackermann function with small values for m and n
print(ackermann(1, 2))  # Expected output: 4
print(ackermann(2, 2))  # Expected output: 7
print(ackermann(3, 1))  # Expected output: 5
