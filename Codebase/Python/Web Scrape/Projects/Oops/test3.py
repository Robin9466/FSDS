class Person:


    def __init__(sudh, name, surname, email_id, year_of_birth):
        sudh.name1 = name
        sudh.surname = surname
        sudh.email_id= email_id
        sudh.year_of_birth = year_of_birth

    def __init__(sudh, name, surname):
        sudh.name1 = name
        sudh.surname = surname
        
    def age(sudh, current_year):
        return current_year - sudh.year_of_birth

anuj_var = Person("anuj", "bhandari", "anuj@email.com",1994)
sudh = Person("sudhanshu", "kumar", "sudhanshu@email.com", 4551)
gargi = Person("gargi", "xyz", "gargi@gmail.com", 4456)

print(sudh.age(2022))
s = "sudh"
s.upper()

