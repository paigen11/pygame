import sys #we will need sys so the user can quit
import pygame #duh

#set up the main core function
def run_game():
	pygame.init()
	size = width, height = 720,540
	speed = [2, 2]
	black = 0, 0, 0
	screen = pygame.display.set_mode(size)
	ball = pygame.image.load("ball.gif")
	ballrect = ball.get_rect()
	print ballrect
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
		ballrect = ballrect.move(speed)
		if ballrect.left < 0 or ballrect.right > width:
			speed[0] = -speed[0]
		if ballrect.top < 0 or ballrect.bottom > height:
			speed[1] = -speed[1]
		screen.fill(black)
		screen.blit(ball, ballrect)
		pygame.display.flip()

run_game() #start the game	