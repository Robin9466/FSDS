class ineuron:
    def __init__(self):
        self.student1 = 'data science'
    def students(self):
        print(self.student1)

i = ineuron()
i.students()
i.student1 = 'data analytics'
i.students()

class ineuron1:
    def __init__(self):
        self.__student1 = 'data science'
    def students(self):
        print(self.__student1)
    def student_change(self, new_value):
        self.__student1 = new_value

i1 = ineuron1()
i1.students()
i1.__student1 = 'big data'
i1.students()
i1.student_change('robin')
i1.students()