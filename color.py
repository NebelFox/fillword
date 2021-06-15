from nebellib.nebeltypes import LoopNumber
from random import randint

class Color:
	# def __init__ (self, r, g, b, shift_distance=16):
	# 	self.r = r
	# 	self.g = g
	# 	self.b = b
	# 	self.shift_distance = shift_distance
	# 	self.random_shift = lambda: self.shift_distance * randint (1, 3) * (-1)**(randint(0, 1))

	def __call__ (self):
		return self.tuple

	def shift (self):
		for i in [self.r, self.g, self.b]:
			i += self.random_shift ()
		self.tuple = (self.r.v, self.g.v, self.b.v)
		# self.r += random_shift ()
		# self.g += random_shift ()
		# self.b += random_shift ()

	def __init__ (self, _hex, shift_distance=16, **kw):
		convert = lambda h: int ('0x'+h, 16)
		r, g, b = convert (_hex[:2]), convert (_hex[2:4]), convert (_hex[4:])
		kw["min"] = 0 if "min" not in kw else kw["min"]
		kw["max"] = 255 if "max" not in kw else kw["max"]
		maxs = "rmax gmax bmax".split ()
		mins = "rmin gmin bmin".split ()
		for key in maxs:
			if key not in kw:
				kw[key] = kw["max"]
		for key in mins:
			if key not in kw:
				kw[key] = kw["min"]
		self.r = LoopNumber (kw["rmin"], kw["rmax"], r)
		self.g = LoopNumber (kw["gmin"], kw["gmax"], g)
		self.b = LoopNumber (kw["bmin"], kw["gmax"], b)
		self.tuple = (self.r.v, self.g.v, self.b.v)
		self.shift_distance = shift_distance
		self.random_shift = lambda: self.shift_distance * randint (1, 10) * (-1)**(randint(0, 1))

	def __repr__ (self):
		print (str(self))

	def __str__ (self):
		return "Color: {} {} {}".format (self.r.v, self.g.v, self.b.v)