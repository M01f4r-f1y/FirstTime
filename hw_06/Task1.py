
#Task 1
print("Input text or number")
a = input()
def t_n(a):
	try:
		float(a)
		print (f"Entered value {a} is a number")
	except ValueError:
		print(f"Entered value {a} is a text")

t_n(a)





