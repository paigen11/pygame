import pygame # duh

class Hero(object):
	def __init__(self, screen):
		self.screen = screen #give the hero the ability to control the screen

		# Load the hero image, get it's rect
		self.image = pygame.image.load('ball.gif')
		self.rect = self.image.get_rect() #pygame gives us get_rect on any object so we can get some dimensions and location
		self.screen_rect = screen.get_rect() #assign a var so the hero class knows how 

		self.rect.centerx = self.screen_rect.centerx #this will put the middle of the hero in the middle of our screen
		self.rect.bottom = self.screen_rect.bottom #this will put our hero "bottom" at the bottom of the screen

		self.moving_right = False #set up movement booleans
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	# add update to the hero class to keep all the hero updates in our hero class
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 10 #move the hero to the right
		elif self.moving_left and self.rect.left > self.screen_rect.left:
			self.rect.centerx -= 10 #move the hero to the left
		elif self.moving_up and self.rect.up < self.screen_rect.up:
			self.rect.centery -= 10 #move the hero up
		elif self.moving_down and self.rect.down > self.screen_rect.down:
			self.rect.centery += 10 #move the hero down	

	def draw_me(self):
		self.screen.blit(source = self.image, dest = self.rect) #draw the surface... (the image, the where)