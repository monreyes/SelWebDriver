"""
Examples to show how string formatting works in python
"""

city = "nyc"
dine = "alingdosya"
event = "show"
#dine = "alingdosya"

print("Welcome to "+city+" and enjoy the "+event+", dont forget to eat at "+dine )
print("Welcome to %s and enjoy the %s, dont forget to eat at %s" % (city,event,dine))
