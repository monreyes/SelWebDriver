"""
A group of code statements which can perform some specific task
Methods are reusable and can be called when needed in the code
"""

def sum_nums(n1, n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2

sum1 = sum_nums(2, 8)

sum2 =  sum_nums(3, 3)

print("*"*20)
print(sum1)
print("*"*20)
print(sum2)
string_add = sum_nums('one ', str(2)) #unless there's the 'str' command, it will yield error
print("*"*20)
print(string_add) # concatenates the 2 string  as per above


print("*************")

def isMetro(city):
    l = ['sfo', 'nyc', 'la']

    if city in l:
        return True
    else:
        return False

x = isMetro('la')
#x = input('What city?')
print(x) # returns "False" if the argument within the method isMetro defined by variable x is not in the "l" list else will return "True"
