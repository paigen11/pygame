# we will put all main game functions here
import sys
import pygame
from bullets import Bullet # we don't care about the update or draw functions. Just the class
from enemy import Enemy

def check_events(hero, bullets, game_settings, screen, play_button):
	for event in pygame.event.get(): #run through all pygame events
		if event.type == pygame.QUIT: #if the event is the quit event...
			sys.exit() #quit
		#handle button click
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			# print mouse_x, mouse_y	
			if play_button.rect.collidepoint(mouse_x, mouse_y):
				game_settings.game_active = True

		elif event.type == pygame.KEYDOWN: #the user pushed a key and it's down
			if event.key == pygame.K_RIGHT: #the user pressed right	
				hero.moving_right = True #set the flag

			elif event.key == pygame.K_LEFT:
				hero.moving_left = True #set the flag

			elif event.key == pygame.K_SPACE: #user pushed space bar
				new_bullet = Bullet(hero, game_settings, screen)
				bullets.add(new_bullet)	

			elif event.key == pygame.K_UP: 	
				hero.moving_up = True 

			elif event.key == pygame.K_DOWN: 	
				hero.moving_down = True 

		elif event.type == pygame.KEYUP: #user let go of a key
			if event.key == pygame.K_RIGHT: #specifically the right arrow
				hero.moving_right = False

			elif event.key == pygame.K_LEFT: 
				hero.moving_left = False

			elif event.key == pygame.K_UP: 
				hero.moving_up = False

			elif event.key == pygame.K_DOWN: 
				hero.moving_down = False				

def update_screen(settings, screen, hero, bullets, enemies, play_button):

	screen.fill(settings.bg_color) #fill the background with our green
	hero.draw_me() #call the draw method and put the hero on our screen
	for enemy in enemies.sprites():
		enemy.draw_enemy()
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	if not settings.game_active:	
		play_button.draw_button()

	pygame.display.flip()


