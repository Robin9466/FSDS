import sys
class Customer:
	'''Customer class with bank related operations'''
	bankname = 'SBI'
	def __init__(self, name, balance=0):
		self.name = name
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		print("After depositing the balance: ",self.balance)

	def withdraw(self, amount):
		if amount > self.balance:
			print("Insufficient balance...")
			sys.exit()
		self.balance -= amount
		print("After withdrawal, amount is: ",self.balance)

# Main program
print("Welcome to ", Customer.bankname)
name = input("Enter your name: ")
print(f"Welcome {name}! in {Customer.bankname}")
c = Customer(name)

while True:
	print('\nChoose an option: ')
	print("d-Deposit\nw-Withdrawal\ne-Exit")
	option = input('Enter your option: ')
	if option.lower() == 'd':
		amount = float(input('Enter the amount to deposit: '))
		c.deposit(amount)
	elif option.lower() == 'w':
		amount = float(input('Enter the withdrawal amount: '))
		c.withdraw(amount)
	elif option.lower() == 'e':
		print('Thanks for banking with us, Visit again')
		sys.exit()
	else:
		print('Try valid option')

