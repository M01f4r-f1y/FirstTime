print("Input text or number")
a = input()
def t_n(a):
	try:
		a = int(a)
		if a % 2 == 0:
			print(f"The number {a} is even")
		else:
			print(f"The number {a} is odd")
	except ValueError:
		n = len (a)
		print (f"{a} is a text and his lenght is {n}")

t_n(a)