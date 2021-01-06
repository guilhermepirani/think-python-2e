''' Draws flowers as in reference 

4.2 Write an appropriately general set of functions that can draw flowers as in Figure'''

import math
import turtle


def arc(t, r, angle):
	'''Draw curved lines'''
	length = 2 * math.pi * r * angle / 360
	n_length = length / 10
	n_angle = angle / 10

	for _ in range(10):
		t.fd(n_length)
		t.lt(n_angle)


def petals(t, r, angle, n):
	'''Transform arcs in n petals'''
	for _ in range(n):
		for _ in range(2):
			arc(t, r, angle)
			t.lt(180 - angle)

		t.lt(360 / n) # make sure flower is a "circle"


if __name__ == '__main__':

	bob = turtle.Turtle()

	petals(bob, 400, 60, 7)
	turtle.mainloop()