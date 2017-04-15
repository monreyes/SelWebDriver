"""
String methods in python
"""

# accessing characters in a string
#index starts from zero
first ="nyc"[0]
city="sfo"
print(first)
ft=city[0]
print(ft)

"""
len()
lower()
upper()
str()
"""

strex = "This is a Mixed Case"
print(strex.lower()) # this command will convert variable strex value into all lower case
print(strex.upper()) # this command will convert variable strex value into all upper case
print(len(strex)) # this command will count the number of characters including spaces of the  variable strex value
print(strex + str(2))

"""
Concatenation
"""

print("Hello" +" "+" World!!!")
print(first+" "+city)
