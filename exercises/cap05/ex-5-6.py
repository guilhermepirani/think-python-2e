'''Code for 5.14.6
The Koch curve is a fractal that looks something like Figure 5.2.
To draw a Koch curve with length x, all you have to do is

Draw a Koch curve with length x/3.
Turn left 60 degrees.
Draw a Koch curve with length x/3.
Turn right 120 degrees.
Draw a Koch curve with length x/3.
Turn left 60 degrees.
Draw a Koch curve with length x/3.
The exception is if x is less than 3: 
in that case, you can just draw a straight line with length x.

Write a function called koch that takes a turtle and a length as parameters, 
and that uses the turtle to draw a Koch curve with the given length.

Write a function called snowflake that draws three Koch curves to make the
outline of a snowflake.
Solution: http://thinkpython2.com/code/koch.py.

The Koch curve can be generalized in several ways.
See http://en.wikipedia.org/wiki/Koch_snowflake for examples
and implement your favorite.'''

import turtle

# Simplest Koch curve, made by me
def koch1(t, x):
	angle = 60
	if x == 0:
		return
	if x >= 3:
		x /= 3

	t.fd(x)
	t.lt(angle)
	t.fd(x)
	t.rt(angle * 2)
	t.fd(x)
	t.lt(angle)
	t.fd(x)

def snowflake(t, x, n = 3):
	'''Repeats Koch curve to draw a snowflake'''
	if n == 0:
		return

	koch2(t, x)
	t.rt(120)
	snowflake(t, x, n - 1)

# Code by Author, change in snowflake to see
def koch2(t, x):
    """Draws a koch curve with length x."""
    if x < 10:
        t.fd(x)
        return
    m = x/3

    koch2(t, m)
    t.lt(60)
    koch2(t, m)
    t.rt(120)
    koch2(t, m)
    t.lt(60)
    koch2(t, m)


bob = turtle.Turtle()

snowflake(bob, 50)
turtle.mainloop()

