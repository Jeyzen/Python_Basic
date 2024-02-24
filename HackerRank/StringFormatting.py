# Given an integer, print the following values for each integer  from  to :

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# Function Description

# Complete the print_formatted function in the editor below.

# print_formatted has the following parameters:

# int number: the maximum value to print
def print_formatted(number): # Print numbers from 1 to number
    width = len(bin(number)[2:]) # Get the length of the binary representation
    for i in range(1, number + 1): # Print the numbers
        decimal = str(i) # Convert the number to a string
        octal = oct(i)[2:] # Convert the number to an octal string
        hexadecimal = hex(i)[2:].upper() # Convert the number to a hexadecimal string
        binary = bin(i)[2:] # Convert the number to a binary string
        print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)