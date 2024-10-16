"""
A spam comment is defined as a text containing following keywords:
"make a lot of money", "buy now", "subscribe this", "click this".
WAP to detect these spams.
"""
comment = input("Enter the comment: ")
comment = comment.lower()

spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

# flag to check if spam is found
is_spam = False

for keyword in spam_keywords:
	if keyword in comment:
		is_spam = True
		break # No need to check further if a spam keyword is found.

if is_spam:
	print("Spam detected")
else:
	print("Spam not detected")class ClassName(object):
		"""docstring for ClassName"""
		def __init__(self, arg):
			super(ClassName, self).__init__()
			self.arg = arg
			
