# WAPP with a recursive approach to calculate the sum of first n natural numbers.

# Define a recursive function to calculate the sum of first n natural numbers
def sum_natural_numbers(n):
    # Base case: if n is 1 or less, return n (because sum of first 1 natural number is 1)
    if n <= 1:
        return n
    # Recursive case: sum of n + sum of first (n-1) natural numbers
    else:
        return n + sum_natural_numbers(n - 1)

# Example: Calculate the sum of the first 5 natural numbers
n = 10
result = sum_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {result}")
