"""
Nested Dictionary:
d = {'k1': {'nestk1':'nestvalue1', 'nestk2': 'nestvalue2'}}
d['k1']['nestk1']
"""

cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}
bmw_year = cars['bmw']['year'] #getting the "year" value for the key "bmw"
print(bmw_year) #printing the value of variable bmw_year
print(cars['benz']['model']) #directly printing(without assigned variable) the "model" value for the key "benz"
