"""
Python Program to Detect Mentions of "Harry"
"""
post = "Harry Potter is my favorite wizard."

# Convert the post to lowercase for case-insensitive matching
post = post.lower()

# Check if "Harry" is a word in the post
if "harry" in post.split():
  print("The post contains 'Harry'.")
else:
  print("The post does not contain 'Harry'.")