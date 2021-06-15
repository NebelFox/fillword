from words_loader import WordsManager
from random import randint
import util
from NebelTypes import LoopNumber

width = 10
height = 10
matrix = list ()
placeholder = ':'
refresh = lambda: [[placeholder]*width for i in range(height)]
# matrix = refresh ()

wm = WordsManager ('words.txt')
wm.load ()

total_len = 75
total_attempts = 0
total_words_generated = 0
total_len_generated = 0


in_bounds = lambda x, y: 0 <= x < width and 0 <= y < height
attempts = 0
for i in range (1000):
	matrix.clear ()
	matrix = refresh ()
	words = list (wm.generate (5, 8, total_len))
	word_index = 0
	while word_index < len (words):

		# debug only
		total_attempts += 1

		attempts += 1
		word = words[word_index]
		ox, oy = randint (0, width-1), randint (0, height-1)
		path = [(ox, oy)]
		is_parsed = True
		for char in word:
			allowed = False
			infinite = False
			start = LoopNumber (0, 3, randint (0, 3))
			counter = 3
			while not allowed:
				dx, dy = util.xy (start*2)
				x, y = ox + dx, oy + dy
				# print ('x: {}, y: {}'.format(x, y))
				get = lambda x, y: matrix[y][x]
				if in_bounds (x, y):
					if matrix[y][x] == placeholder:
						# print ('Allowed: x={}, y={}'.format (x, y))
						allowed = True
						matrix[y][x] = char.upper ()
						ox, oy = x, y
						path.append ((ox, oy))
						continue
				start += 1
				counter -= 1
				if counter < 0:
					infinite = True
					break
			if infinite:
				# print ("infinite")
				is_parsed = False
				break
		if is_parsed:
			word_index += 1
			total_words_generated += 1
			total_len_generated += len (word)
			print ('parsed word: {}'.format (words[word_index-1]))
			for row in matrix:
				print (" ".join (row))

			for row in range (len (matrix)):
				# print ("".join(matrix[row]))
				# print (matrix[row])
				for char in range (len (matrix[row])):
					if matrix[row][char] != ' ' and matrix[row][char].isupper ():
						# print ("replacing {}".format (matrix[row][char]))
						matrix[row][char] = matrix[row][char].lower ()
			# print ('')
			if input () == 'q':
				quit ()
			continue
		# print ("Clearing the unparsed word: {}".format (word))
		print ("Clearing path: ", path)
		for x, y in path:
			matrix[y][x] = placeholder
		path.clear ()

	# for row in matrix: print (row)
	# print ("{} words were generated".format (len(words)))
	# print (words)
	# print ("{} attempts to generate this shit".format (attempts))
	# q = input ()
	# for row in matrix: print (row)
	# if q == 'q':
	# 	for row in matrix: print (row)
	# 	quit ()

	attempts = 0
	# matrix = refresh ()

print ("total_len: {}\ntotal_generated: {}\naverage_len: {}\n".format (
	total_len_generated,
	total_words_generated,
	total_len_generated/1000)
)
print ("Total_appempts: {}\nAverage attempts at one word: {}\nAverage attempts at one matrix: {}".format (
	total_attempts,
	total_attempts/total_words_generated,
	total_attempts/1000)
)
print ("Average words in each matrix: {}\n".format (total_words_generated/1000))

for row in matrix: print (row)
print ('')