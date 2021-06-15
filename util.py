import math

def float_range (start, stop, step):
	stop -= stop%step
	while start < stop:
		yield start
		start += step

def included_range (start, stop, step=1):
	while start <= stop:
		yield start
		start += step

def min_max (first, second, against=0):
	return min (first, against), max (against, second)


def xy (n):
	rad = n*math.pi*0.25
	return round (math.sin(rad)), round (math.cos(rad))

def sign (x):
	if x > 0:
		return 1
	if x < 0:
		return -1
	return 0