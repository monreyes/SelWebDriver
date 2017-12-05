"""
Data type to store more than one value in one variable name
List items are in brackets, separated with "," [ 1, 2, 3 ]
"""

cars = [ "bmw", "honda", "audi"]
empty_list = []
print(empty_list) # will print the empty bracket
print(cars) # this will print whatever values the cars variable has

print("*#"*20) # will print the separators (separator multiplied by 20)

print(cars[1]) # will print the 2nd array within the cars value

num_list = [1, 2, 3]
sum_num = num_list[0] + num_list[1] # the value now adds the 1st array which is "1" and the 2nd array which is "2"

print(sum_num) # will show the value or sum of the equivalent array values i.e. (1+2)=3

more_cars = [ "bmw", "honda", "audi"]
print(more_cars[1]) # will show the value of the 2nd array("honda") within the variable "more cars"

more_cars[1] = "Benz" # this will push(replace) the value of the existing array 1(2nd array)

print(more_cars[1]) # to check, this will show the 2nd array value as "Benz"
print(more_cars) # the whole array will now show the new values (no "honda")
