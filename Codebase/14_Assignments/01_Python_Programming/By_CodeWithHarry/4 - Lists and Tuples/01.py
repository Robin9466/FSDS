"""
WAP to store 7 fruits in the list entered by the user.
"""
fruits = []
i = 0
while i < 7:
	fruit = input("Enter the seven fruits: ")
	fruits.append(fruit)
	i+=1
print(f"Fruits in the list: {fruits}") 