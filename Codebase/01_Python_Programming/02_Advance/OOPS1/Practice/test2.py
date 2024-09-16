class Person:
    def __init__(sudh, name, surname, email_id, year_of_birth):
        sudh.name = name
        sudh.surname = surname
        sudh.email_id = email_id
        sudh.year_of_birth = year_of_birth

# Creating an instance of the Person class
anuj_var = Person("anuj", "bhandari", 'anujbhandari@email.com', 1994)
sudh = Person('sudhanshu', 'kumar', 'sudhanshu@gmail.com', 1997)
gargi = Person('gargi', 'xyz', 'gargi@gmail.com', 1996)

# Accessing and printing the attributes of the instance
print(anuj_var.name)
print(sudh.name)
print(gargi.name)
print(type(sudh))
