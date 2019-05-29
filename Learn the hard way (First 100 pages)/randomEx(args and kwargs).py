# Apperantly there is no increcments are not existing, because it's useless (?)
# so no i++ or i-- in python


# *args and **kwargs

# *args 
def test_var_args(f_arg,*args):
	i = 1
	b = 10
	print("first normal argv:", f_arg)
	for arg in args:
		print(f"arg {i} ", arg)
		print(f"test B {b}")
		i = i+1
		b = b -1
test_var_args(
	'one',
	'two',
	'three',
	'four'
	)

# **kwargs 

def greet_me(**kwargs):
	for key, value in kwargs.items():
		print("{0} = {1}".format(key, value))

greet_me(name = 'slava')