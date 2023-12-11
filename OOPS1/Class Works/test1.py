class Person:


    def __init__(self,name,surname,email_id,year_of_birth):
        self.name = name
        self.surname = surname
        self.email_id = email_id
        self.year_of_birth = year_of_birth

anuj_var = Person("anuj","bhandari","anuj@gmail.com",1994)
sudh = Person("sudhanshu", "kumar","sudhanshu@gmnail.com",898)
gargi = Person("gargi", "xyz","gargi@gmail.com",8988)
print(anuj_var.name)
print(sudh.name)
print(gargi.name)
print(type(sudh))