# WAP to find the factorial of a given number using for loop.

"""
What is factorial?
Answer - A factorial is the product of numbers starting from 1 to till the given number.
"""

# Input from the user
n = int(input("Enter a positive number: "))

# Initialize product
prod = 1

for i in range(1, n+1):
	prod *= i
print("Factorial of the given number is: ", prod)