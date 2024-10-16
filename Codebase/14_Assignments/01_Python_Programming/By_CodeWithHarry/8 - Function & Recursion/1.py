# WAP using function to find greatest of three numbers

def greatest_number(no_list):
	# Assume the first number is the maximum
	max = no_list[0]
	i = 0
	while i < len(no_list):
		if no_list[i] > max:
			max = no_list[i]
		i +=1
	return max
numbers = [14,525,65]
result = greatest_number(numbers)
print(f"The greatest number is: {result}")