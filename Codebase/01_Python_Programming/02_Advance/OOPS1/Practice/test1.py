class Person:
    def __init__(self, name, surname, email_id, year_of_birth):
        self.name = name
        self.surname = surname
        self.email_id = email_id
        self.year_of_birth = year_of_birth

# Creating an instance of the Person class
anuj_var = Person("anuj", "bhandari", 'anujbhandari@email.com', 1994)
sudh = Person('sudhanshu', 'kumar', 'sudhanshu@gmail.com', 1997)
gargi = Person('gargi', 'xyz', 'gargi@gmail.com', 1996)

# Accessing and printing the attributes of the instance
print(anuj_var.name)
print(sudh.name)
print(gargi.name)
print(type(sudh))
