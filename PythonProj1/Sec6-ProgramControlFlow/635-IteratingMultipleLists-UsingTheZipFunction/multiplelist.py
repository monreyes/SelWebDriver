"""
Iterating multiple list at the same time
"""

l1 = [1,2,5,30,25,31]
l2 = [6,2,4,20,30,40]

for a, b in zip(l1,l2):
    if a > b:
        print(a)
    else:
        print(b)
