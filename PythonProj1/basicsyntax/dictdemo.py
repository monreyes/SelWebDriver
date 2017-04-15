"""
Data type to store more than one value in one variable name, in terms of key value pairs
Dictionary items are in brackets {} in key:value pairs, separated with "," {'k1':'v1', 'k2':'v2'}
Not sequenced, no indexing -> Mapping
"""

car = {'make': 'bmw', 'model': '550i', 'year': 2016} #static dictionary
print(car) #prints the value of variable car as it is (random order)

d = {} #defining an empty dictionary

model = car['model'] # gets the value of the internal variable "model" which is "550i"

print(car['make']) #prints the value of the internal variable "make" which is "bmw"
print(model) #prints the value of the variable model which is "550i"

print("*"*25)
print("Adding dictionary values to the empty dictionary 'd' using square brackets")
d['one'] = 1 #assigns separated key and value to a dictionary
d['two'] = 2 #assigns separated key and value to a dictionary

print(d) #prints the key and values of the new dictionary

sum_1 = d['two'] + 8 #adding the value of the dictionary
print(sum_1) #printing the value as adding the item normally
print(d)
d['two'] = d['two'] + 8 #changing the value of the existing dictionary
print(d)
