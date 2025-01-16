class Person2:
    def __init__(self, name, surname, yob):
        self._name = name
        self.__surname = surname
        self.yob = yob

robi = Person2("robin", "kumar", 1997)
print(robi._name)
print(robi._Person2__surname)
