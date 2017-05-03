"""
Examples to show available string methods in python
"""

# Replace Method
a = "1abc2abc3abc4abc"
print(a.replace('abc', 'ABC'))
#print(a.upper()) # another way to convert if all is need to upper case (or a.lower if all needed to be in lower case)

# Sub-Strings
# starting index is inclusive
# Ending index is exclusive
sub = a[1:6]
step = a[1:6:2]

print("****************")

print(sub)
print(step)
