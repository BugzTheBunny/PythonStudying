#This script takes a txt file, and reads it fully, and then a few lines of it. 
#Simple and foolish, because its better to use loops
#But its just one third of the book, so OKAY
from sys import argv 

script, input_file = argv

def print_all(f):
	print(f.read())

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print(line_count, f.readline())

current_file = open(input_file)

print("Full file:")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line+1
print_a_line(current_line, current_file)

current_line = current_line+1
print_a_line(current_line, current_file)

current_line = current_line+1
print_a_line(current_line, current_file)



