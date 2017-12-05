##
#table ref count
##
print("#"*25)
a="nyc"
b="nyc"

print(a)
print("#"*25)
a=123

print(a)
print(b)
print("#"*25)
b=456

print(b)

c='nyc'
d=c
print(c==d)
print(d is c)


x=5
y=2
z=x

print(z)
