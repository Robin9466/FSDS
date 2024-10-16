"""
WAP to input eight numbers from the user, and display unique numbers.
"""

numbers = []
i = 0
while i < 8:
	number = float(input("Enter a number: "))
	numbers.append(number)
	i +=1
unique_numbers = set(numbers)
print("Unique nubmers from the list: ", unique_numbers)
