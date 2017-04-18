"""
1. not
2. and
3. or
"""

print("*"*25)
bool_output = True or not False and False
print("Order of Evaluation for 'True or not False and False'")
print("not False = 'True'")
print("True and False = 'False'")
print("True or False = 'True'")
#  True
print("Final evaluation for boolean 'True or not False and False' is = " + str(bool_output))

print("*"*25)

bool_output_1 = (10 == 10 or not 10 > 10) and 10 > 10
print("showing order of precedence operation for boolean '(10 == 10 or not 10 > 10) and 10 > 10'")
print("1. parentheses operation first")
print("2. 10==10 = 'True'")
print("3. not 10 > 10 = 'True'")
print("4. 'True' or 'True' = 'True'")
print("5. 10>10 = 'False'")
print("'True' and 'False' = 'False'")
print("The boolean evaluation for '(10 == 10 or not 10 > 10) and 10 > 10' is "+ str(bool_output_1))

# True or True -> True and False -> False
print(bool_output_1)
