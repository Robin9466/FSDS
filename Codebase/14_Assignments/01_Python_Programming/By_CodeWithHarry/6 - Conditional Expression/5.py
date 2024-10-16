"""
WAP to find out whether a given name is present in the list or not.
"""

name_list = ['robin', 'vikash', 'deepak', 'sharwan', 'neeraj']

name = input("Enter a name: ")

# convert input name to lower for case-insensitive comparision
name_lower = name.lower()

is_found = False

# Check if the entered name is found in the list
for item in name_list:
	if item.lower() == name_lower:
		is_found = True
		break # Exit the loop if loop is found

# Output the result
if is_found:
	print("Name found")
else:
	print("Name not found")