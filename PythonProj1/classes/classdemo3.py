"""
Object Oriented Programming
"""

class Car(object):

    wheels = 4 #attribute of the class Car (common, member variable(instance variables))

    def __init__(self, carmake, carmodel, caryear ='2017'):
        self.make = carmake #attributes
        self.model = carmodel
        self.year = caryear

    def info(self):
        print("Make of the car: " + self.make)
        print("Model of the car: " + self.model)
        print("Year of the car: " + self.year)



c1 = Car('bmw', '550i')
# print(c1.make) #prints the 'make' as per the class 'Car'
# print(c1.year) # prints the default year as the initial (init) method parameters
c1.info() # this method prints the attributes/values of the car 'info' method  as per supplied argument (note: class reference c1
# did not provide year argument, thus it will take the default value as per initial (init)

print("*"*25)


c2 = Car('benz', 'E350', '2012')
#print(c2.make)
c2.info() # this prints the attributes/values of the car info as per supplied argument (note: class reference c2
# has been provided with a year argument, thus it will overwrite the default value as per initial (init)

print("*"*25)

print(c2.make) # this one did not call the method 'info', thus it will directly print whatever the value of the 'make'
# in the c2 reference values


print("*"*25)



print(Car.wheels)
