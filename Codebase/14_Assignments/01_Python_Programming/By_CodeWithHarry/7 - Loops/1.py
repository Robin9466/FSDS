"""
WAP to print multiplication table of a given number using for loop.
"""

number = int(input("Enter for which you want a table: "))

for i in range(10):
	print(number*(i+1))