def add(a,b):
	print(f"Add {a} + {b}")
	return a+b

def substract(a, b):
	print(f"Substract {a} - {b}")
	return a-b

def multiply(a,b):
	print(f"Multiply {a} * {b}")
	return a*b

def divide(a,b):
	print(f"divide {a} / {b}")
	return a / b

a = add(20,3)
b = substract(10,2)
c = multiply(2,10)
d = divide(90,3)

print(f"{a} {b} {c} {d}")

e = add(a, substract(b,multiply(c, divide(d,3))))
print(e)