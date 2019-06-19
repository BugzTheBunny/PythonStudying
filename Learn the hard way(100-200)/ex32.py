ten_things = "Apples Oranges Crows Telephone Light Sugar"
print(ten_things)
print("Wait, there are not 10 things in that list, lets fix it!")

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("Adding: ",next_one)
	stuff.append(next_one)
	print(f"There are {len(stuff)} items now")

print("Thre we go: ", stuff)

print("Let's play with the list")
print(stuff[1])
print(stuff[-1]) #!?!?!?
#.pop removes the las item.
#Can be helpfull if you are reading things from a file, and you dont need the last item that the script just added.
print(stuff.pop())
print(stuff.pop())
print(stuff.pop())
print(stuff.pop())
print(stuff)
print(' '.join(stuff)) #?
print(' BETWEEEENN '.join(stuff[3:5]))

