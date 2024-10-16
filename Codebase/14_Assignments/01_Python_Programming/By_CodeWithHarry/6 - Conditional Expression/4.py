"""
WAP to find whether a given username contains less than 10 characters or not.
"""
string = input("Input a username: ")

count = 0
index = 0
while index < len(string):
	count +=1
	index +=1

if count < 10:
	print("username is less than 10 characters")
else: 
	print("username is greater than 10 characters") 
