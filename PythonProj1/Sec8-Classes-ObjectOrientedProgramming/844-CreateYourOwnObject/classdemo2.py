"""
Object Oriented Programming
"""

class Car(object):

    def __init__(self, carmake = "Sarao", carmodel = 'leps', caryear = '2015'):
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


print("*$"*15)
c3 = Car('toyota','Rav4')
print(c3.make.upper())
print(c3.model.upper())
print(c3.year)

print("*$"*15)
c4 = Car('Honda','Civic' ,'2013')
print(c4.make.upper())
print(c4.model.upper())
print(c4.year)

print("*$"*15)
c5 = Car()
print(c5.make.lower())
print(c5.model.upper())
print(c5.year)
