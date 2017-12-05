"""
Class demo - inheritance 2 (method over riding)
"""


class Car(object): #base class

    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped")



class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("You just created the BMW instance")

    def drive(self): #overrides the parent method class
        super(BMW, self).drive() #calling the base method class
        print("You are driving a BMW, Enjoy...")

    def headsup_display(self):
        print("This is a unique feature")


class Toyota(BMW):

    def __init__(self):
        Car.__init__(self)
        print("You just created the Toyota instance")

    def drive(self): #overrides the parent method class
        #super(Toyota, self).drive() #calling the parent method class BMW
        #The above will print 'You are driving a BMW, Enjoy...'
        print("You are driving a reliable car Toyota, go far...")

    def headsup_display(self):
        print("This is a diff feature - grandchild of Car,and child of BMW")



print("*"*25)
print("Printing parent class 'Car' attributes")
print("-/-"*10)
c = Car() #assigning parent class to a variable
c.drive()
c.stop()


print("*" * 25)
print("*" * 25)
print("Printing child class 'BMW' attributes")
print("-/-" * 10)
b = BMW()
b.drive()
b.stop()
b.headsup_display()

print("*" * 25)
print("*" * 25)
print("Printing child class 'Toyota' (child of BMW) attributes")
print("-/-" * 10)
t = Toyota()
t.drive()
t.stop()
t.headsup_display()
