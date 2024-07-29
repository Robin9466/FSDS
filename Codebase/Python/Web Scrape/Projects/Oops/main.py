class Person:


    def __init__(self, name, surname, email_id, year_of_birth):
        self.name1 = name
        self.surname = surname
        self.email_id= email_id
        self.year_of_birth = year_of_birth

anuj_var = Person("anuj", "bhandari", "anuj@email.com", 1994)
sudh = Person("sudhanshu", "kumar", "sudhanshu@email.com", 4551)
gargi = Person("gargi", "xyz", "gargi@gmail.com", 4456)
print(anuj_var.name1)
print(sudh.name1)
print(gargi.name1)
print(type(sudh))
