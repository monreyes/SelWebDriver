"""
Built-in methods to help manipulating a list
"""

cars = [ "bmw", "honda", "audi"]

length = len(cars) # count the number of items inside the cars variable
print(length) # will show the number of items(after each comma) within the variable length

print("*"*25)
print("Appending values(append=end of the list)")
cars.append("Benz") # will append (on the end) the value "Benz"
print(cars) # shows that the "Benz" now is added at the end of the variable values of "cars"

print("*"*25)
print("Inserting values anywhere in the list")
cars.insert(1, "Jeep") # this will insert the value as per the argument provided in 2nd index(array) of "cars"
print(cars) # will now show cars with the value "Jeep" as the 2nd index instead of "Honda"

print("*"*25)
print("Finding the index as per argument provided")
x = cars.index("honda") # finding the index of honda
print(x) # shows where "honda" is

print("*"*25)
print("Popping the item from the last in the list (note: when an argument index num has been provided, the item will be the one to pop out")
y = cars.pop() # removes (pop) the last item in the list(when no index num has been provided)
print(y) # last item show as "Benz"
print(cars) # shows the updated cars list where the last item "Benz" is no longer in the list

cars.remove("Jeep") # selectively removing the item in the argument within the list
print(cars) # shows the updated cars list where "Jeep" is no longer in the list


print("*"*25)
print("Slicing the index list")
print(cars)
print("Now, we're slicing cars[0:2]")
slicing = cars[0:2] # This will only include the beginning[0] of the index but will exclude index[2]
a = cars[1:]
print(slicing)
print(a)

print("*#"*20)
print(cars)
cars.sort() # sorts the list ascending

print(cars)
