######################
#ex25
print("-----\nex25:\n-----")
######################
people = 20
cats = 30
dogs = 15

if  people < cats:
	print("Too many cats!")

if people > cats:
	print("Small amount of cats! The world is saved!")

if people < dogs:
	print("The world is drooled on!")
if people > dogs:
	print("The world is dry!")

dogs += 5

if people >= dogs:
	print("People are greater or equal to dogs!")
if people <= dogs:
	print("People are less or equal to dogs!")
if people == dogs:
	print("People are dogs(?)")


######################
#ex26
print("-----\nex26:\n-----")
######################

people = 30
cars = 40
trucks = 15

if cars > people:
	print("We should take the cars.")
elif cars < people:
	print("We should not take the cars.")
else:
	print("We cant decide.")

if trucks > cars:
	print("Too many trucks!")
elif trucks < cars:
	print("Too many cars")
else:
	print("We still can't decide.")

if people > trucks:
	print("Alright, let's just take the trucks.")
else:
	print("Fine, let's stay home!")

######################
#ex27
print("-----\nex27:\n-----")
######################

print("""You enter a dark room with two doors.
Do you go through door 1 or door 2?
	""")
door = input("(1) or (2)? >")

if door == "1":
	print("There's a giant bear here eating a cheese cake.")
	print("What do you do?")
	print("""
		1. take the cake.
		2. Scream at the bear.
		""")

	bear = input("(1) or (2)? >")
	if bear == "1":
		print("The bears ate you, good job!")
	elif bear == "2":
		print("The bear only ate your head, good job!")
	else:
		print("Smaaarrttt, you are saved!")

elif door == "2":
	print("You stare into teh endless abyss at Chtulhu's retina.")
	print("1. BlueBerries.")
	print("2. Yellow jacket clothspins.")
	print("3. Understanding revolvers telling melodies")

	insanity = input("(1) or (2) or (3)? ==>")

	if insanity == "1" or insanity == "2":

		print("Your body survives powered by a mind of jello.")
		print("Good Job!")
	else:
		print("The insanity rots your eyes into a pool of muck.")
		print("Good job!")
else:
	print("You went back and died, great!")