
import pygame #duh
from hero import Hero #bring in the hero class with all its methods and glory
from settings import Settings
import game_functions as gf

#set up the main core function
def run_game():
	pygame.init() # initialize all the pygame modules
	game_settings = Settings() #create an instance of settings class
	screen = pygame.display.set_mode(game_settings.screen_size) #set the screen size with set_mode
	pygame.display.set_caption("Monster Attack") #set the message on the status bar
	hero = Hero(screen) # set a variable equal to the class and pass it the screen

	while 1: #run this loop forever...
		gf.check_events(hero) #call gf (aliased from game_functions module) and get the check_events
		hero.update() #update the hero flags
		gf.update_screen(game_settings, screen, hero) # call the update_screen method
				

run_game() #start the game	