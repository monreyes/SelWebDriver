"""
Built-in function
Creates a sequence of numbers but does not save them in memory
Very useful for generating numbers
"""

a = range(0, 20, 6) #where 0 is the starting point and 20 is the exclusive end point, 6 is the step
print(a)#prints the value of a as range
print(type(a)) #will show the class as "range"

print(list(a)) #prints the list (excludes the last number)


l = [1, 2, 3]

for num in range(1, 5): #note that this range has now nothing to do with the list "l"
    print(num)
