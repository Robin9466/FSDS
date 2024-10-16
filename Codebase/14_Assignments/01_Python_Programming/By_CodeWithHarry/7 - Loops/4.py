"""
WAP to find whether a given number is prime or not.
"""

"""num = int(input("Enter a number: "))

if num <=1:
	print("Not a prime")

elif num == 2 or num == 3:
	print("prime")

else:
	for i in range(2, num):
		if num % i == 0:
			print("Not a prime number")
			break
	else:
		print("prime")
"""
# Loop optimization: 
import math
num = int(input("Enter a number: "))

if num <=1:
	print("Not a prime")

elif num == 2 or num == 3:
	print("prime")

else:
	for i in range(2, int(math.sqrt(num) + 1)):
		if num % i == 0:
			print("Not a prime")
			break
	else:
		print("prime")