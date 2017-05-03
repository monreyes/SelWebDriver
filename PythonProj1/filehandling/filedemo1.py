"""
File I/O
'w' -> Write-Only Mode
'r' -> Read-only Mode
'r+' -> Read And Write Mode
'a' -> Append Mode
"""

my_list = [1, 2, 3, 4]

my_file = open("firstfile2.txt", "w") #this will create a file(current dir) and write the content of the list in it

for item in my_list:
    my_file.write(str(item) + "\n")
print("firstfile2.txt has been written as per below details")
my_file.close()

print("//"*15)
my_fileToWrite = open("firstfile2.txt", 'r')
print(str(my_fileToWrite.read()))
my_fileToWrite.close()


