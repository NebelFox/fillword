from random import randint

class WordsManager:
	def __init__ (self, path):
		self.path = path
		self.data = []
		self.len = 0
		self.max_len = 0
		self.min_len = 0

	def load (self):
		with open (self.path, 'r') as file:
			self.data = file.read ().split ('\t')
		# print (self.data)
		self.len = sum ([len(word) for word in self.data])
		self.max_len, self.min_len = max ({len(w) for w in self.data}), min ({len(w) for w in self.data})

	def shuffle (self):
		for i in range (len(self.data)):
			j = randint (0, i)
			self.data[i], self.data[j] = self.data[j], self.data[i]

	def a_few (self, count):
		selected = []
		while count > 0:
			index = self.index ()
			if index not in selected:
				selected.append (index)
				count -= 1
				yield self.data[index]

	def index (self):
		return randint (0, len (self.data)-1)

	def one (self):
		return self.data[self.index ()]

	def generate (self, min_len, max_len, total_len):
		min_len = max (self.min_len, min_len)
		max_len = min (self.max_len, max_len)
		selected = []
		while total_len > 0:
			index = self.index ()
			if index not in selected:
				selected.append (index)
				word = self.data[index]
				l = len (word)
				if min_len <= l <= max_len:
					if total_len - l < 0:
						if total_len - l < -l//2:
							yield word
						return
					total_len -= l
					yield word