from sys import argv
#Part 2 of the exercise, making a smaller file
#The first argument will be the file name, that is "ex12Part2.py"
#meaning that variable a is the name of the script.
a,b,c = argv

print(f"Calling this script {a}")
print(f"Second argument{b}")
print(f"Third argument{c}") 

#argv : to use when you want to input the text in the command line
#input() : to use when you want the user to input the text while the script is running
name = input("Enter your name: ")
print(f"Your name is {name}")
