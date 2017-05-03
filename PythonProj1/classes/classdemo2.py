"""
Object Oriented Programming
"""

class Car(object):

    def __init__(self, carmake, carmodel = 'leps', caryear = '2015'):
        self.make = carmake
        self.model = carmodel
        self.year = caryear

print("*$"*15)
c1 = Car('bmw','i3')
print(c1.make)
print(c1.model)
print(c1.year)

print("*$"*15)
c2 = Car('benz','leps','2012')
print(c2.make)
print(c2.model)
print(c2.year)
