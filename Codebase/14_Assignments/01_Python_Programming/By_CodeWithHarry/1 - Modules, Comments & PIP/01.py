"""
WAP to list out the directoris using OS modules
"""

import os

# Specifying the directory of the path:
directory_path = r"C:\Users\Robin Raj\CodeHub\FSDS"

# Read the contents of the directory
try:
	contents = os.listdir(directory_path)

	# Print each item in the directory
	for item in contents:
		print(item)
except FileNotFoundError:
	print(f"The directory '{directory_path}' does not exist")