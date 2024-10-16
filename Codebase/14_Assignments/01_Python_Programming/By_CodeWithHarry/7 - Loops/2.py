"""
WAP to greet all the person names stored in a list l1 and which starts with S.
"""

l1 = ["Harry", "Sohan", "Sachin", "Rahul"]

for name in l1:
	if name[0].lower() == "S".lower():
		print("Hello", name)