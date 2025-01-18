class Person:


    def __init__(sudh,name,surname,email_id,year_of_birth):
        sudh.name = name
        sudh.surname = surname
        sudh.email_id = email_id
        sudh.year_of_birth = year_of_birth

    def __init__(sudh,name,surname,email_id,year_of_birth):
        sudh.name = name
        sudh.surname = surname
        sudh.email_id = email_id
        sudh.year_of_birth = year_of_birth

    def age(sudh, current_year):
        return current_year - sudh.year_of_birth

anuj_var = Person("anuj","bhandari","anuj@gmail.com",1994)
sudh = Person("sudhanshu", "kumar","sudhanshu@gmnail.com",898)
gargi = Person("gargi", "xyz","gargi@gmail.com",8988)

print(anuj_var.age(2022))
