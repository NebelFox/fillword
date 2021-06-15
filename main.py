import pygame
import random
import os
from nebellib.nebeltypes import LoopNumber, BoundNumber
from wordfiller import generate
from words_loader import WordsManager
from color import Color

pygame.init ()

# GRID_WIDTH = BoundNumber.adjust (6, 20, int (input ("Enter the grid width (6-20): ")))
# GRID_HEIGHT = BoundNumber.adjust (6, 20, int (input ("Enter the grid height (6-20): " )))
GRID_WIDTH, GRID_HEIGHT = 12, 12
CEIL_SIZE = int (120* (6 / max(GRID_HEIGHT, GRID_WIDTH)))
WIDTH, HEIGHT = GRID_WIDTH * CEIL_SIZE, GRID_HEIGHT * CEIL_SIZE
print (WIDTH, HEIGHT)

screen = pygame.display.set_mode ((WIDTH, HEIGHT))
clock = pygame.time.Clock ()

font_name = pygame.font.match_font ('arial')

wm = WordsManager ('words.txt')
wm.load ()

placeholder = ''
len_mult = BoundNumber (0, 1, 0.5)
total_len = int(GRID_WIDTH*GRID_HEIGHT*len_mult)
min_len, max_len = wm.min_len, wm.max_len

color = Color ("440000", min=0, max=127)
color.shift()
# print (color)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

words = list(wm.generate (min_len, max_len, total_len))


def draw_text (surface, text, x, y, size, color):
	font = pygame.font.Font (font_name, size)
	text_surface = font.render (text, True, color)
	text_rect = text_surface.get_rect ()
	text_rect.center = (x, y)
	surface.blit (text_surface, text_rect)

def draw_rect (surface, x, y, width, height, color):
	rect = pygame.Rect (x, y, width, height)
	pygame.draw.rect (surface, color, rect)

screen.fill ((0, 0, 0))
def draw_grid ():
	for i in range (GRID_WIDTH+1):
		draw_rect (screen, i*CEIL_SIZE-2, 0, 4, HEIGHT, WHITE)
	for i in range (GRID_HEIGHT+1):
		draw_rect (screen, 0, i*CEIL_SIZE-2, WIDTH, 4, WHITE)

ceil_rect = lambda x, y: pygame.Rect (x*CEIL_SIZE+2, y*CEIL_SIZE+2, CEIL_SIZE-4, CEIL_SIZE-4)


# print (words)
matrix, paths = generate (GRID_WIDTH, GRID_HEIGHT, words, placeholder, False)

def draw_letter (x, y, char):
	if char != placeholder:
		x = x * CEIL_SIZE + CEIL_SIZE // 2
		y = y * CEIL_SIZE + CEIL_SIZE // 2
		draw_text (screen, char.upper (), x, y, int (CEIL_SIZE*0.75), color())
# index = 0
def draw_matrix ():
	for i in range (GRID_HEIGHT):
		for j in range (GRID_WIDTH):
			draw_letter (j, i, matrix[i][j])

def refresh ():
	screen.fill((0, 0, 0))
	draw_grid ()
	draw_matrix ()
	pygame.display.flip ()
# refresh ()

def won_screen ():
	screen.fill ((0, 0, 0))
	draw_text (screen, "You won!", WIDTH//2, HEIGHT//2, 100, color() )
	pygame.display.flip ()
# pygame.display.flip ()

def print_words (_words):
	# os.system ('cls')
	print ("Words left: {}".format (len(_words)))
	for i in range (len(_words)):
		# print (i)
		print (_words[i].ljust (max_len+1), end='')
		if i%3 == 2:
			print ()

def update_ceils (color, *ceils):
	for x, y in ceils:
		draw_rect (screen, x*CEIL_SIZE+2, y*CEIL_SIZE+2, CEIL_SIZE-4, CEIL_SIZE-4, color)
		draw_letter (x, y, matrix[y][x])
	pygame.display.update ([ceil_rect (x, y) for x, y in ceils])

def tick ():
	clock.tick (60)
	for event in pygame.event.get ():
		if event.type == pygame.QUIT:
			return False
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			return False
	return True

print_words (words)

screen.fill (BLACK)
draw_grid ()
draw_matrix ()
pygame.display.flip ()

mouse_path = []
# last_broken = (None, None)
# was_broken = False

running = True
won = False
print ("starting while loop")
while running:

	running = tick ()

	pressed = pygame.mouse.get_pressed ()[0]
	relx, rely = pygame.mouse.get_rel ()

	if pressed and (relx or rely):
		# if relx or rely:
		mouse_x, mouse_y = pygame.mouse.get_pos ()
		mouse_x, mouse_y = mouse_x - relx, mouse_y - rely
		pos = (mouse_x // CEIL_SIZE, mouse_y // CEIL_SIZE)
		if (pos not in mouse_path):
			mouse_path.append (pos)
			update_ceils (RED, pos)
		elif len (mouse_path) >= 2 and pos == mouse_path[-2]:
			update_ceils (BLACK, mouse_path.pop (-1))
		elif len (mouse_path) >= 4 and pos in mouse_path[:-2]:
			# last_broken = pos
			pressed = False
			# was_broken = True

	if not pressed and mouse_path:
		# print (mouse_path)
		if mouse_path in paths:
			
			selected = [matrix[y][x] for x, y in mouse_path]
			words.remove ("".join(selected))
			paths.remove (mouse_path)
			for x, y in mouse_path:
				matrix[y][x] = placeholder
			print_words (words)
		update_ceils (BLACK, *mouse_path)
		mouse_path.clear ()

	if not words:
		won = True
		running = False

if won:
	won_screen ()
	while tick ():
		pass