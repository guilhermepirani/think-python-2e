''' Draws an Archimedian spiral '''

import turtle

def spiral(t, n, lenght, r, whirl):
	'''
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