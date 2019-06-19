the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears', 'apricots']
change =[1, 'pennis', 2, 'dimes', 3,'quarters']

for number in the_count:
	print(f"number: {number}")


for fruit in fruits:
	print(f"fruit: {fruit}")


for i in change:
	print(f"i = {i}")
	
#Creating a new array out of everything
elements = []

for i in the_count:
	elements.append(i)
for i in fruit:
	elements.append(i)
for i in change:
	elements.append(i)

print(elements)