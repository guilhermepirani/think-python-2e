'''Code for 5.14.3
If you are given three sticks, you may or may not be able to arrange
them in a triangle.
For example, if one of the sticks is 12 inches long and the
other two are one inch long,
you will not be able to get the short sticks to meet in the middle.
For any three lengths, there is a simple test to see
if it is possible to form a triangle:

If any of the three lengths is greater than the sum of the other two,
then you cannot form a triangle.
Otherwise, you can. (If the sum of two lengths equals the third,
they form what is called a “degenerate” triangle.)

1) Write a function named is_triangle that takes three integers as arguments,
and that prints either “Yes” or “No”, depending on whether you can or cannot
form a triangle from sticks with the given lengths.

2) Write a function that prompts the user to input three stick lengths,
converts them to integers, and uses is_triangle to check whether sticks
with the given lengths can form a triangle. '''
def check_input(i):
	'''Validate user input as integer'''
	if i.isalpha():
		i = 0
		return i
	else:
		return int(i)

def  is_triangle(a, b, c):
	'''Calculate if 3 sticks can form a triangle by their length in inches'''
	if a > (b + c) or b > (a + c) or c > (a + b):
		print("No")
	else:
		print("Yes")

def sticks_triangle():
	a = b = c = 0
	while a <= 0:
		a = input("Enter any number for a: ")
		a = check_input(a)
	while b <= 0:
		b = input("Enter any number for b: ")
		b = check_input(b)
	while c <= 0:
		c = input("Enter any number for c: ")
		c = check_input(c)

	is_triangle(a, b, c)

sticks_triangle()