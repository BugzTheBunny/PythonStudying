#Simple whileloops (Added casting ot make it a function).
#Added color just to know how to.
import colorama
colorama.init()


i = 0
o = int(input("Enter a number > "))
x = int(input("Increment by...? > "))
numbers = []

def loop_this(o,i,x):
	print("TEST")
	while i < o:
		print(f"\033[31m At the top i is {i}")
		numbers.append(i)

		i=i+x
		print("Numbers now: ", numbers)
		print(f"Ath the bottom i is {i}")
	print("The humbers: ")

	for num in numbers:
		print(num)

loop_this(o,i,x)
print("Done!")

