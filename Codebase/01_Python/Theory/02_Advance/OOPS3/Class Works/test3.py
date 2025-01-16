class ineuron:
    def student(self):
        print(f'print the details of all the students')
    def acheivers(self):
        print(f'print the list of all the achiever')
    def hall_of_fame(self):
        print(f'print everyone from hall of fame')

class ineuron_vision(ineuron):
    def student(self):
        print(f'these are the filtered student lists')

iv = ineuron_vision()
iv.student()
