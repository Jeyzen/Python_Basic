# Task

# You are given two values  and .
# Perform integer division and print .

# Input Format

# The first line contains , the number of test cases.
# The next  lines each contain the space separated values of  and .

# Constraints

# Output Format

# Print the value of .
# In the case of ZeroDivisionError or ValueError, print the error code.

# Function to handle integer division or errors
def perform_division(a, b):
    try:
        result = int(a) // int(b)  # Perform integer division
        print(result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

# Input the number of test cases
test_cases = int(input().strip())

# Iterate through each test case
for _ in range(test_cases):
    # Input the values for the test case
    a, b = input().split()
    # Perform division for the current test case
    perform_division(a, b)