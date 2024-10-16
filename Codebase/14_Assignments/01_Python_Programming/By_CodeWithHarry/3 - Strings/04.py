"""
WAP to Fill in a Letter Template with Name and Date:
"""
name = input("Enter your name: ")
date = input("Enter the date (e.g., 2024-10-09): ")

letter = f"""Dear {name}, 
					You are selected !
					{date}
					"""
print(letter)