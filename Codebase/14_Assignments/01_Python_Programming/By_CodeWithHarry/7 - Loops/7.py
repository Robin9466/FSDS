"""
WAP to print the following star pattern:

   *
  ***
 *****

"""

"""
For printing patterns, Use 3 following thumb rule:
1. No of rows = No of times outer loop will run
2. No of columns = No of times inner loop will run
3. What do you want to print.
"""

n = 3
# For handling spaces:
for s in range(n):
	print(' '*(n-s-1), end = '')
for i in range(n):
	print('*'*(2 * i + 1))

