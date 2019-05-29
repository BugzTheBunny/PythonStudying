# Instatiating a variable
types_of_people = 10
# Instatiating a variable with the previuos one formated inside of it
x = f"there are {types_of_people} types of people"
# Instatiating a variable
binary = "binary"
# Instatiating a variable
do_not = "don't"
# Instatiating a variable with the last two formatted inside of it
y = f"Those who know {binary} and those {do_not}"
# printing x
print(x)
#printing y
print(y)
# printing two lines with x / y formatted inside of them.
print(f"I said: {x}")
print(f"I also said: {y}")

#setting hilarious as False (boolean)
hilarious = False
# Instatiating a variable with an empty place for string formatting inside of it
joke_evaluation = "Isn't that joke so funny?! {}"
#printing (inserting hilarious inside of the empty space in the string)
print(joke_evaluation.format(hilarious))
#Setting two variables
w = "This is the left side of..."
e = "a string with a right side"
#printing w and e
#it makes a longer string, because i used + instead of "," and that combined the strings
print(w + e)
#now it wont combine them into one, but will pring both of them
print(w , e)