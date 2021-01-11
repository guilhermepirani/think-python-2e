'''Code for 5.14.1
The time module provides a function, also named time,
that returns the current Greenwich Mean Time in “the epoch”,
which is an arbitrary time used as a reference point. On UNIX systems,
the epoch is 1 January 1970.

>>> import time
>>> time.time()
1437746094.5735958

Write a script that reads the current time and converts it
to a time of day in hours, minutes, and seconds,
plus the number of days since the epoch. '''

'''From documentation: 
time() returns as a floating point number expressed in seconds'''

import time

ticks = time.time()

def now(t):
	'''Returns actual GMT time and days since epoch'''
	h_since = int(t // 60 // 60)
	h_now = h_since - (h_since // 24) * 24
	min_since = int(t // 60)
	min_now = min_since - (min_since // 60) * 60
	sec_since = int(t // 1)
	sec_now = sec_since - (sec_since // 60) * 60

	days = int(t // 60 // 60 // 24)
	return f"{h_now}:{min_now}:{sec_now} It's been {days} days since epoch"

print(now(ticks))