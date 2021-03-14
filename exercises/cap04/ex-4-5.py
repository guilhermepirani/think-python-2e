''' Code for 4.12.5
Read about spirals at http://en.wikipedia.org/wiki/Spiral;
then write a program that draws an Archimedian spiral 
(or one of the other kinds). '''

import turtle

def spiral(t, n, lenght, r, whirl):
	''' Draws an Archimedian spiral
	n is for how long the turtle works, use big numbers
	lenght is the space in which the curvature is applyed, use small integers
	whirl is the overall curvature, use .3-4f decimals
	r affects the innermost curvature, use .1f decimals
	'''
	angle = 0

	for _ in range(n):
		t.fd(lenght)
		n_angle = 1 / (r + whirl * angle)

		t.lt(n_angle)
		angle += n_angle

bob = turtle.Turtle()

spiral(bob, 1000, 3, 0.1, 0.0002)
turtle.mainloop()