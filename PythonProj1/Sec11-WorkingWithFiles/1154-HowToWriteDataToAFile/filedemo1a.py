

"""
File I/O
'w' -> Write-Only Mode
'r' -> Read-only Mode
'r+' -> Read And Write Mode
'a' -> Append Mode
"""

import datetime

cur_datetime = datetime.datetime.now().strftime("%m%d%Y-%H%M")

my_list = [8, 4, 3, 2]
print(my_list[-1])
filedemo1a = 'filedemo1a-'+ str(cur_datetime) +'.txt'

my_file = open(filedemo1a, "w") #this will create a file(current dir) and write the content of the list in it

for item in my_list:
    my_file.write(str(item * my_list[-1]) + "\n")
print(filedemo1a + " has been written as per below details")
my_file.close()

print("//"*15)
my_fileToWrite = open(filedemo1a, 'r')
print(str(my_fileToWrite.read()))
my_fileToWrite.close()


