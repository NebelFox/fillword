# class EADict(dict):
# 	def __init__ (self, **kwargs):
# 		self.__origin_attributes = self.__dict__.keys ()
# 		print (self.__origin_attributes)
# 		super().__init__ (**kwargs)
# 	def __getattr__(self, name):
# 		if name in self:
# 			return self[name]

# 	# def __setattr (self, name, value):


# d = EADict (a=10, b=12)
# print (d.a)

class NumberBase:
	def __init__ (self, _min, _max, value):
		self.min = _min
		self.max = _max
		if self.min > self.max:
			self.min, self.max = self.max, self.min
		self.v = self.min if value is None else value

	@property
	def v (self):
		return self.value

	def set (self, value):
		if self.min <= value <= self.max:
			self.value = value
			return True
		return False

	def set_to_min (self):
		self.value = self.min

	def set_to_max (self):
		self.value = self.max

	def __add__ (self, other):
		if isinstance (other, NumberBase):
			return self.v + other.v
		return self.v + other

	def __radd__ (self, other):
		return self.v + other

	def __iadd__ (self, other):
		if isinstance (other, NumberBase):
			self.v += other.v
			return self
		self.v += other
		return self

	def __sub__ (self, other):
		if isinstance (other, NumberBase):
			return self.v - other.v
		return self.v - other

	def __rsub__ (self, other):
		return self.v - other

	def __isub__ (self, other):
		if isinstance (other, NumberBase):
			self.v -= other.v
			return self
		self.v -= other
		return self

	def __mul__ (self, other):
		if isinstance (other, NumberBase):
			return self.v * other.v
		return self.v * other

	def __rmul__ (self, other):
		return self.v * other

	def __imul__ (self, other):
		if isinstance (other, NumberBase):
			self.v *= other.v
			return self
		self.v *= other
		return self

	def __ifloordiv__ (self, other):
		if isinstance (other, NumberBase):
			self.v //= other.v
			return self
		self.v //= other
		return self

	def __rfloordiv__ (self, other):
		return self.v // other

	def __floordiv__ (self, other):
		if isinstance (other, NumberBase):
			return self.v // other.v
		return self.v // other

	def __itruediv__ (self, other):
		if isinstance (other, NumberBase):
			self.v /= other.v
			return self
		self.v /= other
		return self

	def __rtruediv__ (self, other):
		return self.v / other

	def __truediv__ (self, other):
		if isinstance (other, NumberBase):
			return self.v / other.v
		return self.v / other

	def __mod__ (self, other):
		if isinstance (other, NumberBase):
			return self.v % other.v
		return self.v % other

	def __rmod__ (self, other):
		return self.v % other

	def __imod__ (self, other):
		if isinstance (other, NumberBase):
			self.v %= other.v
			return self
		self.v /= other
		return self

	def __pow__ (self, other):
		if isinstance (other, NumberBase):
			return self.v ** other.v
		return self.v ** other

	def __rpow__ (self, other):
		return self.v ** other

	def __ipow__ (self, other):
		if isinstance (other, NumberBase):
			self.v **= other.v
			return self
		self.v **= other
		return self

	def __pos__ (self):
		return +self.v

	def __neg__ (self):
		return -self.v

	def __round__ (self, n=0):
		return round (self.v, n)

	def __int__ (self):
		return int (self.v)

	def __float__ (self):
		return float (self.v)

	def __str__ (self):
		return str (self.v)

	def __hash__ (self):
		return int (self.v)

	def __abs__ (self):
		return abs (self.v)

	def __call__ (self):
		return self.v

	def __repr (self):
		return str (self.v)


class LoopNumber (NumberBase):
	formula = lambda _min, _max, value: _min + (value-_min)%(abs (_max-_min)+1)
	def __init__ (self, _min, _max, value=None):
		self.differ = self.make_differ (_min, _max)
		super ().__init__ (_min, _max, value)

	@NumberBase.v.setter
	def v (self, value):
		if not self.set (value):
			self.value = self.min + (value-self.min)%self.differ

	@staticmethod
	def adjust (_min, _max, value):
		if _min <= value <= max:
			return value
		differ = LoopNumber.make_differ (_min, _max)
		result = _min + (value-_min)%differ
		return result

	@staticmethod
	def make_differ (_min, _max):
		return abs (_max - _min) + 1


class BoundNumber (NumberBase):
	def __init__ (self, _min, _max, value=None):
		super ().__init__ (_min, _max, value)

	@NumberBase.v.setter
	def v (self, value):
		if not self.set (value):
			self.value = max (self.min, min (self.max, value))

	@staticmethod
	def adjust (_min, _max, value):
		if _min <= value <= _max:
			return value
		return max (_min, min (_max, value))