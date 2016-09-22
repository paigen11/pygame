
import pygame #duh
from hero import Hero #bring in the hero class with all its methods and glory
from enemy import Enemy
from settings import Settings
import game_functions as gf
from pygame.sprite import Group

#set up the main core function
def run_game():
	pygame.init() # initialize all the pygame modules
	game_settings = Settings() #create an instance of settings class
	screen = pygame.display.set_mode(game_settings.screen_size) #set the screen size with set_mode
	pygame.display.set_caption("Monster Attack") #set the message on the status bar
	hero = Hero(screen) # set a variable equal to the class and pass it the screen
	enemies = Group()
	bullets = Group() #set bullets
	enemies.add(Enemy(screen, game_settings))

	tick = 0

	while 1: #run this loop forever...
		tick += 1

		if tick % 150 == 0:
			enemies.add(Enemy(screen, game_settings))

		gf.check_events(hero, bullets, game_settings, screen) #call gf (aliased from game_functions module) and get the check_events
		hero.update() #update the hero flags
		enemies.update(hero, game_settings.enemy_speed)
		bullets.update() #call the update method in the while loop
		gf.update_screen(game_settings, screen, hero, bullets, enemies) # call the update_screen method
		
		for enemy in enemies:
			for bullet in bullets: # get rid of bullets that are off the screen
				if bullet.rect.bottom <= 0: #bullet bottom is at the top of the screen
					bullets.remove(bullet) #call remove()
				if len(bullets) >= 10:
					bullets.remove(bullet)
				if enemy.rect.colliderect(bullet.rect):
					enemies.remove(enemy)
					bullets.remove(bullet)
			if enemy.rect.colliderect(hero.rect):
				print "The monster got you! You died!"
				exit(0)		
							
run_game() #start the game	