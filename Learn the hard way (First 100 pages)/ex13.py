from sys import argv 

script, user_name = argv
promt = '>'

print(f"Hi {user_name}, I am {script}.")
print("I'd like you to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(promt)

print(f"Where do you live {user_name}")
lives = input(promt)

print(f"What kind of a PC do you use {user_name}?")
pc = input(promt)

print(f"""
	Allright, so you said {likes} about liking me,
	You live in {lives}. Not sure where that is,
	And you have a {pc} computer, nice.
	""")