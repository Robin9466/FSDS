class Person:


    def __init__(self, name, surname, email_id, year_of_birth):
        self.name = name
        self.surname = surname
        self.email_id= email_id
        self.year_of_birth = year_of_birth

anuj_var = Person("anuj", "bhandari", "anuj@email.com", 1994)
print(anuj_var.name)
print(anuj_var.surname)
print(anuj_var.email_id)
