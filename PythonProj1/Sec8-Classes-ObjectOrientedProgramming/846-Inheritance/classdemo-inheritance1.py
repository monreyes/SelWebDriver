"""
Class demo - inheritance 1
"""
class Car(object):

    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped")

class BMW(Car): # child class 'BMW' inherits the parent class 'Car' method attributes

    def __init__(self):
        Car.__init__(self) # this will print the comment from the initial method of the parent class (__init__(self))
        print("You just created the BMW instance")

print("*"*25)
print("Printing parent class 'Car' attributes")
print("-/-"*10)

c = Car() #creating(printing) the instance of the class 'Car' through __init__ self
c.drive() #calling(printing) the method attribute 'drive' within the class 'Car'
c.stop() #calling(printing) the method attribute 'stop' within the class 'Car'

print("*"*25)
print("Printing 'BMW' attributes as inherited through parent class 'Car'")
print("-/-"*10)
b = BMW() #creating(printing) the instance of the class 'BMW' through __init__ self inherited from parent class 'Car'
b.drive() #calling(printing) the method attribute 'drive' from parent class 'Car' inherited by child class 'BMW'
b.stop() #calling(printing) the method attribute 'stop' from parent class 'Car' inherited by child class 'BMW'


