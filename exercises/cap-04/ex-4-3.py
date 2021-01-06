''' Draws polygons as in reference 

4.3 Write an appropriately general set of functions that can draw shapes as in Figure'''

import math
import turtle

def triangle(t, length, angle, n):
	for _ in range(n):
		for _ in range(2):
			t.lt(angle)
			t.fd(length)

		t.lt(360 / n)


if __name__ == '__main__':

	bob = turtle.Turtle()

	triangle(bob, 100, 60, 6)
	turtle.mainloop()