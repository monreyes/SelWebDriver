"""
Dictionary Methods
"""

car = {'make': 'bmw', 'model': '550i', 'year': 2016} #static dictionary (3 keys, 3 values)
cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}} #nested dictionary (2 keys, 2nested values)
a=car.keys()
print(a)
print(car.keys()) #list all the 'keys' for the dictionary called car
print(cars.keys()) #list all the 'keys' for the dictionary called cars
print(car.values()) #list all the 'values' for the dictionary called car
print(cars.values()) #list all the 'values' for the dictionary called cars
print(car.items()) #listing all items for dictionary car

car_copy = car.copy() #copying the dictionary
print(car_copy)

print(car.pop('model')) #pops out key model
print(car)
