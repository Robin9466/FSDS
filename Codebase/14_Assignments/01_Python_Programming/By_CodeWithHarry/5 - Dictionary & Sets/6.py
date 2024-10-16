"""
Create an empty dictionary, and allow 4 friend to enter their language as value, and name as the key, assume the names to be unique.
"""
friends_language = {}
i = 0
while i < 4:
	name = input("Enter your name: ")
	language = input(f"Enter {name}'s language: ")
	i +=1

	friends_language[name] = language
print(friends_language)