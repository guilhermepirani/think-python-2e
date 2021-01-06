''' Draws polygons as in reference 

4.3 Write an appropriately general set of functions that can draw shapes as in Figure'''

import math
import turtle

def triangle(t, syze, angle):
	'''Draws isosceles triangle'''
	y = syze * math.sin(angle * math.pi / 180)

	t.lt(angle)
	t.fd(syze)
	t.rt(90 + angle)
	t.fd(2 * y)
	t.rt(90 + angle)
	t.fd(syze)
	t.rt(180 - angle)

def polygons(t, sides, syze):
	''' draw triangles sharing sides '''
	angle = 360 / sides
	for _ in range(sides):
		triangle(t, syze, angle/2)
		t.rt(angle)


if __name__ == '__main__':

	bob = turtle.Turtle()

	# Change sides to print each polygon from reference
	# polygons(bob, 5, 300)
	# polygons(bob, 6, 300)
	polygons(bob, 7, 300)
	turtle.mainloop()