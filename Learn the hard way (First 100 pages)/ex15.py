# Fucntions - 
# 	close - closes the file 
#	read - reads from a file, can be assigned to a line
#	readline - reads one line from the text file
#	truncate - empties the file
#	write('') - writes into a file
#	seek(0) - move the read/write location to the beginning of the line
from sys import argv
script, filename = argv 

print(f"We're going to erase {filename}.")
print("If you don't want that press ctrl-c (^C).")
print("If you do want that, press return")

input("?")

print("Opening file...")
target = open(filename, 'w')
print("truncating the file...Goodbye!")
target.truncate()

print("Now please input three lines")

line1 = input(">")
line2 = input(">")
line3 = input(">")

print("Im going to write all of this into a file...")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And im closing it")
target.close()