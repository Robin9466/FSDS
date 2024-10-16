"""
WAP to print a hollow diamond star patten:
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
 """
n = int(input("Enter number of rows for the hollow diamond: "))

# Upper part of the diamond:
for i in range(n):
    # Print leading spaces
    print('  ' * (n - i - 1) + '* ', end='')  
    # Print hollow spaces in between stars
    if i >= 1:
        print('  ' * (2 * i - 1) + '* ', end='')
    print()

# Lower part of the diamond:
for i in range(n-1):
    # Print leading spaces
    print('  ' * (i + 1) + '* ', end='')
    # Print hollow spaces in between stars
    if i != (n - 2):  # Avoid printing star at the end in the last row
        print('  ' * (2 * (n - i - 2) - 1) + '* ', end='')
    print()
