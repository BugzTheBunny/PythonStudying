from sys import exit 
import colorama
colorama.init()

def gold_room():
	print("This room is full of gold. How much do you take?")

	choice = int(input("> "))
	if (choice> 1 & choice < 50):
		print("""
			Woaahhh, you are o kind!
			You could take more!!
			""")
		exit(0)
	elif(choice > 50 & choice < 100 ):
		print("Awesome! you are not greedy, you win!")
		exit(0)
	elif(choice > 100):
		dead("You are greedyyyy......")
	else:
		dead("Learn to write a number....")

def bear_room():
	print("""
		\033[33m
		There is a bear here!
		The bear has a bunch of honey.
		The fat bear is in front of another door.
		""")
	bear_moved = False


	while True:
		choice = input("> ")

		if choice == 'take honey':
			dead('The bear looks at you, then slaps your face off.')
		elif choice == 'taunt bear' and not bear_moved:
			print("""
				The bear has moved from the door.
				You can go through it now!
				""")
			bear_moved = True
		elif choice == 'taunt bear' and bear_moved:
			print("The bear gets pissed off and eats your face.")
		elif choice == 'open door' and bear_moved:
			gold_room()
		else:
			print("You had one job!")
			bear_room()

def chtulhu_room():
	print("""
		\033[32m
		Here you see the great evil chtulhu
		He, it, whatever stares at you and you go insane.
		Do you flee for your life, or eat your head?
		""")

	choice = input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well, that was tasty!")
	else:
		chtulhu_room()

def dead(why):
	print(why, "Good job!")
	exit(0)

def start():
	print("""
		\033[31m
		You are in a dark room
		There is a room to you right and to you left
		Which one do you take?
		""")

	choice = input("> ")

	if choice == 'left':
		bear_room()
	elif choice == 'right':
		chtulhu_room()
	else:
		dead()

start()