"""
WAP to find the sum of first n natural numbers using while loop.
"""

n = int(input("Enter the number, For which you want to see the first n natural number: "))

sum = 0
i = 1
while i <= n:
	sum = sum + i
	i +=1
print("Sum of first n natural number is: ", sum)