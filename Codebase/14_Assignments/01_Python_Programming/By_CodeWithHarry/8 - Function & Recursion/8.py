# WAP function to print multiplication table of a given number.

def print_multiplication_table(number, up_to=10):
    # Loop to generate the multiplication table up to the given limit
    for i in range(1, up_to + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

# Example usage:
num = 7  # You can change this to any number
print_multiplication_table(num)
