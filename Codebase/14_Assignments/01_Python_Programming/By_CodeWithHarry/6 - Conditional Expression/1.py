"""
WAP to find greatest of four numbers entered by the user.
"""
numbers = []
i = 0
while i < 4:
	number = int(input("Enter the number: "))
	numbers.append(number)
	i +=1
print(f"Number entered by you is {numbers}")

greatest_number = numbers[0]
i = 1
while i < 4:
	if numbers[i] > greatest_number:
		greatest_number = numbers[i]
	i +=1
print("Greatest number from the list is: ", greatest_number)