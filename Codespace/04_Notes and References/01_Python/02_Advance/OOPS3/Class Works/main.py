class Car:

    def __init__(self, body, engine, tyre):
        self.body = body
        self.engine = tyre
        self.tyre = tyre

    def milage(self):
        print(f'milage of this car')

c = Car('solid', 'v6', 'radial')
print(c)

class Tata(Car):
    pass

t = Tata('solid', 'v7', 'radial1')
print(t)
print(t.milage())