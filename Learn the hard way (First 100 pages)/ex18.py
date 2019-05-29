# Creating a function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"you have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes!")
	print("Man, thats enough for a party!")
	print("Get a blanket.\n")
####	Calling the function
print("We can just give the fucntion numbers directly:")
cheese_and_crackers(20,30)

####	Calling again
print("OR, we can use variables from our script")
xcheese_count = 10
xboxes_of_crackers = 15
cheese_and_crackers(xcheese_count,xboxes_of_crackers)

###		Calling again
cheese_and_crackers(11-3, 5+3)
###		And again...
cheese_and_crackers( + 5, boxes_of_crackers + 99)
