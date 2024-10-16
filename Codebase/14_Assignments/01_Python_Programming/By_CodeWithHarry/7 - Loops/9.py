"""
WAP to print the following star pattern:

* * *
*   *
* * *
"""

n = 3

# for handling pattern:
for i in range(n):
	for j in range(n):
		if i == 0 or i == 2 or j == 0 or j == 2:
			print('* ')
		else:
			print(' ')