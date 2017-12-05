"""
With / As Keywords
"""

import datetime

cur_datetime = datetime.datetime.now()#.strftime("%m%d%Y-%H%M")
formatdatetime = cur_datetime.strftime("%m%d%Y-%H%M")



########################################################
##Comment this block when running/executing the below
# print("Normal Write Start")
# my_write = open("textfile.txt", "w")
# my_write.write("Trying to write to the file")
# my_write.close() #this line allows the below code to be executed
#
#
# print("Normal Read Start")
# my_read = open("textfile.txt", "r")
# print(str(my_read.read())) #this will print the content as per whatever has been recently written by the code to textfile.txt

#########################################################
"""
This block of code no longer needs the 'close' keyword
"""
##Comment this block when running/executing the above
withas = "withas-"+str(formatdatetime)+".txt"
print("With As Write Start")
with open(withas, "w") as with_as_write:
    with_as_write.write("This is an example of with as write/read, with server based current time filenaming\n")
    with_as_write.write("This file was written on " + str(formatdatetime) + "H")
print()
print("With As Read Start")
with open(withas, "r") as with_as_read:
    print(str(with_as_read.read()))
#########################################################
