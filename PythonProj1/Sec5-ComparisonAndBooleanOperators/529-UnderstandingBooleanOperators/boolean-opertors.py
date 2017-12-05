"""
and
**************************************
True and True   --> True
True and False  --> False
False and False --> False
**************************************

or
**************************************
True or True   --> True
True or False  --> True
False or False --> False
**************************************

not
**************************************
Not True  --> False
Not False --> True
"""


print("%"*25)
print("Showing boolean operator results for 'AND'")
and_output1 = (10 == 10) and (10 > 9)
print("The logical/boolean operator output for '(10 == 10) and (10 > 9)' is " + str(and_output1))
#print(and_output1)  + print("and_output1 = (10 == 10) and (10 > 9)")
and_output2 = (10 == 10) and (10 < 9)
print("The logical/boolean operator output for '(10 == 10) and (10 < 9)' is " + str(and_output2))
and_output3 = (10 > 10) and (10 < 9)
print("The logical/boolean operator output for '(10 > 10) and (10 < 9)' is " + str(and_output3))

print("%"*25)
print("Showing boolean operator results for 'OR'")
or_output1 = (10 == 10) or (10 > 9)
print("The logical/boolean operator output for '(10 == 10) or (10 > 9)' is " + str(or_output1))
or_output2 = (10 == 10) or (10 < 9)
print("The logical/boolean operator output for '(10 == 10) or (10 < 9)' is " + str(or_output2))
or_output3 = (10 > 10) or (10 < 9)
print("The logical/boolean operator output for '(10 > 10) or (10 < 9)' is " + str(or_output3))


print("%"*25)
print("Showing boolean operator results for 'NOT'")
not_true = not (10 == 10)
print("The logical/boolean operator output for 'not (10 == 10)' is " + str(not_true))
not_false = not (10 > 10)
print("The logical/boolean operator output for 'not (10 > 10)' is " + str(not_false))

print(not_false)
