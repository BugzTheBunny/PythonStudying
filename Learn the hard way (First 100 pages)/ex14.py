#This script reads simple text files, in this case .
# this ment to read "ex14_sample.txt", so that should be the filename.


#Import
from sys import argv 
#Setting
script, filename = argv
#txt is reading everything from the file you input, and becomes that (a string)
#
txt = open(filename)
#prints the information the line above recived
print(f"Here's your file{txt}:")
print(txt.read())

#The rest is boring af
print("Type file name again: ")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())

txt.close()
txt_again.close()

print("closed the files")