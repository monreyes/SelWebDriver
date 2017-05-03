"""
Class demo - inheritance 2 (method over riding)
"""


class Fruit(object): #base/parent class

    def __init__(self):
        print("You just created the Fruit instance")

    def nutrition(self):
        print("A fruit a day is beneficial to our health...")

    def fruit_shape(self):
        print("Most fruits are round in shape..")


class Tomato(Fruit): #child class

    def __init__(self):
        Fruit.__init__(self)
        print("You just created the Tomato instance")

    # def nutrition(self):
    #     print("A fruit a day is beneficial to our health...")

    def fruit_shape(self):
        print("Tomato is round in shape")

    def fruit_color(self):
        print("It is red when ripe")

class Apple(Fruit): #child class of parent class 'Fruit'

    def __init__(self):
        Fruit.__init__(self)
        print("You just created the Apple instance")

    # def nutrition(self):
    #     print("A fruit a day is beneficial to our health...")

    def fruit_shape(self):
        print("Apples are like heart in shape")

    def fruit_color(self):
        print("It is shiny red when ripe")

    def fruit_taste(self):
        print("Sweet and Crunchy")


class GreenApple(Apple): #child class of parent class 'Apple'

    def __init__(self):
        Apple.__init__(self) # this will call both the base class init for 'Fruit' and parent class init for 'Apple'
        #since class 'Apple' is a child of 'Fruit' class
        print("You just created the GreenApple instance")

    # def fruit_shape(self):
    #     print("Apple is like heart in shape")

    def fruit_color(self):
        print("GreenApple is still green when ripe")

    def fruit_taste(self):
        print("Sweet, Sour and Crunchy")

f = Fruit()
f.nutrition()
f.fruit_shape()

print("#*"*15)
print("#*"*15)
t = Tomato()
t.nutrition()
t.fruit_shape()
t.fruit_color()

print("#*"*15)
print("#*"*15)
a = Apple()
a.nutrition()
a.fruit_shape()
a.fruit_color()
a.fruit_taste()


print("#*"*15)
print("#*"*15)
g = GreenApple()
g.nutrition()
g.fruit_shape()
g.fruit_color()
g.fruit_taste()
