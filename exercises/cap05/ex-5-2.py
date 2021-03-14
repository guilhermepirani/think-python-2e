'''Code for 5.14.2
Fermat’s Last Theorem says that there are no positive integers a, b, 
and c such that:
a**n + b**n = c**n 
for any values of n greater than 2.

Write a function named check_fermat that takes four parameters—a, b, c and n
—and checks to see if Fermat’s theorem holds.
If n is greater than 2 and a**n + b**n = c**n 
the program should print, “Holy smokes, Fermat was wrong!” 
Otherwise the program should print, “No, that doesn’t work.”

Write a function that prompts the user to input values for a, b, c and n, 
converts them to integers, and uses check_fermat to check whether they
violate Fermat’s theorem.'''
def check_input(i):
	if i.isalpha():
		i = 0
		return i
	else:
		return int(i)

def check_fermat():
	'''Try inputs to check if they validate fermat's theorem'''
	print("Calculate if: positives a**n + b**n = c**n when n > 2")
	a = b = c = n = 0
	while a <= 0:
		a = input("Enter any number for a: ")
		a = check_input(a)
	while b <= 0:
		b = input("Enter any number for b: ")
		b = check_input(b)
	while c <= 0:
		c = input("Enter any number for c: ")
		c = check_input(c)
	while n <= 2:
		n = input("Enter any number for n: ")
		n = check_input(n)

	abp_sum = a ** n + b ** n

	if abp_sum == c ** n:
		print(abp_sum, "and", c ** n, '!', "Holy smokes, Fermat was wrong!\n")
	else:
		print(abp_sum, "and", c ** n, '!', "No, that doesn’t work.\n")

check_fermat()