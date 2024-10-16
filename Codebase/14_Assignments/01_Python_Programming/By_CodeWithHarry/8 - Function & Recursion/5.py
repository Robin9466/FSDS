"""
# WAPP using function to print first n lines of the following pattern:
* * *
* * 
*
"""

# Define a function to print the pattern
def print_pattern(n):
    # Outer loop to iterate through the lines
    for i in range(n, 0, -1):
        # Print '*' i times on each line
        print("* " * i)

# Example: Call the function to print the first 3 lines of the pattern
n = 3
print_pattern(n)
