"""
https://docs.python.org/3/library/
"""
import math
from math import sqrt
# import sys
# sys.path
# sys.path.append(C:\Users\rreyes.FARM\AppData\Local\Programs\Python\Python35-32\Lib\importlib)
from modulesexternal.car import info


class ModulesDemo():

    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(100))

    def car_description(self):
        make = "bmw"
        model = "550i"
        type = "Sedan"
        info(make, model, type)


m = ModulesDemo()
#m.builtin_modules()
m.car_description()
