"""
A group of code statements which can perform some specific task
Methods are reusable and can be called when needed in the code
"""
def sum_nums(n1, n2):
    print(n1 + n2)
    print(n1*n2)

print("*"*20)
sum_nums(2, 8) #This will call the operation under the method

print("*"*20)
sum_nums(3, 3) #This will call (again) the operation under the method

print("*"*20)
l = [1, 2, 3]
print(len(l))

print("*"*20)
print(l.append(4)) #this will show as "None" since it only commands to append the number 4 to  the list
print(l) # will show the updated list with the appended number

print("*"*20)
print(len(l))
