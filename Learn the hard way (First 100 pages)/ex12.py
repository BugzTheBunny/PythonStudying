from sys import argv
# Has to be started from a commant line "python ex12.py arg arg2 arg3"
# If you wont insert the 3 arguments in the command above, it will give you an error.
# In teh case you insert not enough arguments, Python will send another error, that will explain what is wrong.
script, first, second, third = argv

print("This script is called: ", script)
print("The first var is: ", first)
print("The second var is: ", second)
print("Your third var is: ", third)