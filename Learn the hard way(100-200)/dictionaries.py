#Creating a dictionary
import colorama
def br():
	print('~'*25,'|')
def br2():
	print('---'*2)

states ={
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
}

#Basic set of states and some sities in them.
cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#Print out some cities
br()
print("NY State has: " ,cities['NY'])
print("OR State has: " ,cities['OR'])

#Print some states
br()
print("Michigan has:",cities[states['Michigan']])
print("Florida has:",cities[states['Florida']])

#Print every state abbreviation 
br()
for state, abbrev in list(states.items()):
	br2()
	print(f"{state} has city {abbrev}")
br()

for abbrev, city in list(cities.items()):
	br2()
	print(f"{abbrev} has the city {city}")
br()

for state, abbrev in list(states.items()):
	br2()
	print(f"{state} is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}")

br()
state = states.get("Texas")
if not state:
	print("Sorry, no Texas.")

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
#Best way to add items to a dictionary, if there is the same key, it will be overwritten.
states['IL'] = 'Israel'
states['RU'] = 'Russia'
states['EG'] = 'Egypt'
br()
print(states)
