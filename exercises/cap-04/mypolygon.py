# Page 31: 4.3 Exercises
''' final code at 4.3.5
 Make a more general version of circle called arc that takes an additional
parameter angle, which determines what fraction of a circle to draw.
 The parameter angle is in units of degrees,
so when angle=360, arc should draw a complete circle.
'''
import math
import turtle

def square(t, lenght):
	for _ in range(4):
		t.fd(lenght)
		t.lt(90)

def polygon(t, length, n):
	for _ in range(n):
		t.fd(length)
		t.lt(360 / n)

def circle(t, r):
	length = (2 * math.pi * r) / 120
	polygon(t, length, 120)

def arc(t, r, angle):
	length = 2 * math.pi * r * angle / 360
	n = int(length / 3) + 1
	n_length = length / n
	n_angle = angle / n

	for _ in range(n):
		t.fd(n_length)
		t.lt(n_angle)

if __name__ == '__main__':

	bob = turtle.Turtle()

	arc(bob, 50, 180)
	turtle.mainloop()

# Step through to final code 

''' code for 4.3.1
 Write a function called square that takes a parameter named t,
which is a turtle.
 It should use the turtle to draw a square.
 Write a function call that passes bob as an argument to square,
and then run the program again.

def square(t):
	for _ in range(4):
		t.fd(100)
		t.lt(90)

square(bob)
'''

''' code for 4.3.2
 Add another parameter, named length, to square.
 Modify the body so length of the sides is length,
and then modify the function call to provide a second argument.
 Run the program again. Test your program with a range of values for length.

def square(t, lenght):
	for _ in range(4):
		t.fd(lenght)
		t.lt(90)

square(bob, 100)
'''

''' code for 4.3.3
 Make a copy of square and change the name to polygon.
 Add another parameter named n and modify the body so it draws an n-sided
regular polygon. 
 Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.

-- def polygon -- 
polygon(bob, 100, 10)
'''

''' code for 4.3.4
 Write a function called circle that takes a turtle, t, and radius, r,
as parameters and that draws an approximate circle by calling polygon with an
appropriate length and number of sides. 
 Test your function with a range of values of r.
 Hint: figure out the circumference of the circle 
and make sure that length * n = circumference.

global --> PI = 3.14159265359
 -- def circle --
circle(bob, 100)
'''