"""WAP to detect double spaces in a string.
"""

string = "Hi, how are you,  Robin?"
double_spaces_index = string.find("  ")

if double_spaces_index != -1:
	print(f"Double spaces detected at index: {double_spaces_index}")
else:
	print(f"No double spaces found")