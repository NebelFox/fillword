import pygame
pygame.init ()
info  = pygame.display.Info ()

# font_name = pygame.font.match_font ('arial')
# def draw_text (surface, text, x, y, size, color):
# 	font = pygame.font.Font (font_name, size)
# 	text_surface = font.render (text, True, color)
# 	text_rect = text_surface.get_rect ()
# 	text_rect.center = (x, y)
# 	surface.blit (text_surface, text_rect)

SIZE = WIDTH, HEIGHT = (320, 180)
# SIZE = (0, 0)
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
clock = pygame.time.Clock ()
screen = pygame.display.set_mode (SIZE)
# pygame.draw.rect (screen, (51, 53, 94), pygame.Rect (20, 20, 100, 100))
pygame.display.update ()
last_update = 0
last_dur = 0

running = True
while running:
	clock.tick (FPS)
	now = pygame.time.get_ticks ()
	cur_dur = now - last_update
	last_update = now

	if cur_dur != last_dur:
		print (cur_dur)
		last_dur = cur_dur
	for event in pygame.event.get ():
		# ((10523551//53352)*5163)%152
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			running = False
	# x, y = pygame.mouse.get_pos ()
	# screen.fill (BLACK)
	# pygame.draw.circle (screen, WHITE, pygame.mouse.get_pos (), 5)

	# pygame.display.update ()