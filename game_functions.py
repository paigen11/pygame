# we will put all main game functions here
import sys
import pygame

def check_events(hero):
	for event in pygame.event.get(): #run through all pygame events
		if event.type == pygame.QUIT: #if the event is the quit event...
			sys.exit() #quit
		elif event.type == pygame.KEYDOWN: #the user pushed a key and it's down
			if event.key == pygame.K_RIGHT: #the user pressed right	
				hero.moving_right = True #set the flag
			elif event.key == pygame.K_LEFT:
				hero.moving_left = True #set the flag
			elif event.key == pygame.K_UP: 	
				hero.moving_up = True #set the flag	
			elif event.key == pygame.K_DOWN: 	
				hero.moving_down = True #set the flag		
		elif event.type == pygame.KEYUP: #user let go of a key
			if event.key == pygame.K_RIGHT: #specifically the right arrow
				hero.moving_right = False
			elif event.key == pygame.K_LEFT: 
				hero.moving_left = False
			elif event.key == pygame.K_UP: 
				hero.moving_up = False	
			elif event.key == pygame.K_DOWN: 
				hero.moving_down = False				

def update_screen(settings, screen, hero):
	screen.fill(settings.bg_color) #fill the background with our green
	hero.draw_me() #call the draw method and put the hero on our screen
	pygame.display.flip()


