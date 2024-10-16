# WAPP using using function to convert Celsius to Farenheit.

def celcius_fahrenheit(cel_temp):
	fahr_temp = 9/5*cel_temp + 32
	return fahr_temp

result = celcius_fahrenheit(0)
print("Your temperature in fahrenheit is: ", result)