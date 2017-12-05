"""
Tuple
Like list but they are immutable
It means you can't change them
"""

my_list = [1, 2, 3]
print(my_list) #will show list as it is

my_list[0] = 0 #assigning a new value on the index 0 (1st index)
print(my_list) #will show list with the 1st index as 1(before) being replaced by 0

my_tuple = (1, 2, 3, 2, 2, 3) #tuples are in parenthesis while list are inside square brackets
print(my_tuple) #will show as it is

print("trying to assign a value to a tuple")
#my_tuple[0]=0   ->tuple does not support item assignment
print(my_tuple[0]) #will show the 1st item in the index

print(my_tuple[1:]) #will print from 2nd index up to last

print(my_tuple.index(2)) #will show the index number of the item '2' (which is 1(index))

print(my_tuple.count(3)) #shows how many instances of 3 in the tuple
