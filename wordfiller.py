from random import random, randint
import util
from nebellib.nebeltypes import LoopNumber

chars = "qwertyuiopasdfghjklzxcvbnm"
chance = 0.5

def generate (width, height, words, placeholder=' ', debug=False):

	matrix = [[placeholder]*width for i in range (height)]
	yields = []

	in_bounds = lambda x, y: 0 <= x < width and 0 <= y < height

	# print (words)

	word_index = 0

	while word_index < len (words):

		word = words[word_index]
		ox, oy = randint (0, width-1), randint (0, height-1)
		path = []
		is_parsed = True
		prev_dir = None
		for char in word:
			allowed = False
			infinite = False
			prev_dir = randint (0, 3) if prev_dir is None or random () > chance else prev_dir
			start = LoopNumber (0, 3, prev_dir)
			counter = 3
			while not allowed:
				dx, dy = util.xy (start*2)
				x, y = ox + dx, oy + dy
				get = lambda x, y: matrix[y][x]
				if in_bounds (x, y):
					if matrix[y][x] == placeholder:
						allowed = True
						matrix[y][x] = char
						ox, oy = x, y
						path.append ((ox, oy))
						continue
				start += 1
				counter -= 1
				if counter < 0:
					infinite = True
					break
			if infinite:
				is_parsed = False
				break
		if is_parsed:
			word_index += 1
			yields.append (path)
			continue

		for x, y in path:
			matrix[y][x] = placeholder
		path.clear ()
	if not debug:
		for i in range (height):
			for j in range (width):
				if matrix[i][j] == placeholder:
					matrix[i][j] = chars[randint(0, len(chars)-1)]
	return matrix, yields