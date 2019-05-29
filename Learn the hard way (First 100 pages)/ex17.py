# Creating functions

#One way of working.
#print1 intakes arguments (as much as the function needs to build args)
#and then uses them and prints them
def print1(*args):
	arg1, arg2, arg3, arg4 = args
	print(f"{arg1} {arg2} {arg3} {arg4}")
#second way of working
def print2(arg1, arg2,arg3,arg4):
	print(f"arg1: {arg1} arg2: {arg2}......")

#Same as last one but with one argument
def print3(arg1):
	print(f"arg1: {arg1}")

#no arguments intake 

def print4():
	print("Empty")

print1("Slava","KTZ","LS","FF")
print2("a","b","c","d")
print3("One arg")
print4()

###############################################################
print("-----------------------------")
#Self test (Trying a for loop?)
#This intakes arguments and works as print1, but it iterates in args like a list, and prints them one by one in a for loop
def print5(*args):
	arg1, arg2, arg3, arg4 = args
	for arg in args:
		print(f"Will work? {arg}")

#Calling my little function
print5("one","two","ten","five")