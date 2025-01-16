class Person:

    def __init__(sudh, name, surname, email_id, year_of_birth):
        sudh.name = name
        sudh.surname = surname
        sudh.email_id = email_id
        sudh.year_of_birth = year_of_birth

    def __init__(sudh, name,surname):
        sudh.name = name
        sudh.surname = surname

    def age(sudh, current_year):
        return current_year


anuj_var = Person("anuj", "bhandari")
sudh = Person("sudhanshu", "kumar")
gargi = Person("gargi", "xyz")

print(anuj_var.age(2022))
