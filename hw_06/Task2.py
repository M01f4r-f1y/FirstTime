print("Input the number")

a = input()
def n_p(a):
	try:
		a = int(a)

		if a % 2 == 0:
			print(f"The number {a} is even")
		else:
			print(f"The number {a} is odd")
	except ValueError:
		print(f"The value {a} is not a number")

n_p(a)

