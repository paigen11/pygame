#What is it?
--- 
A simple, monster killing game built in Python through the Pygame modules. Users can start the game, which comes equipped with music and sound effects, shoot bullets to kill monsters which head towards them and keep track of how many monsters they've killed.

##Languages Used
---
  * Python

##Link to Github
---
[Github](https://github.com/paigen11/pygame)

##Author
---
Paige Niedringhaus

##Screenshots
---
Start screen when users load up the game
![alt text]()

Game play screen of enemies coming for the player
![alt text]()

Bullets used to kill enemies and rack up points on the score counter
![alt text]()

##Further Info
---
Through the use of the Pygame modules and some fairly simple Python-based code this whole game was created.

##Requirements
---
You'll need to install Python on your system if you don't already have it - my system's running on Python 2 not 3, which can be downloaded [here](https://www.python.org/downloads/).

After that, in order to install Pygame, you'll need to make sure your pip and setuptools are up to date, which can be done through the instructions [here](https://packaging.python.org/installing/).

Finally, you can install the Pygame modules using these instruction [here](http://www.pygame.org/wiki/CompileUbuntu)

##Code Examples
---
Python code that keeps the game running and updating as it runs
```python
	while 1: #run this loop forever
			gf.check_events(hero, bullets, game_settings, screen, play_button) #call gf (aliased from game_functions module) and get the check_events
			gf.update_screen(game_settings, screen, hero, bullets, enemies, play_button, scoreboard) # call the update_screen method
			if game_settings.game_active:
				hero.update() #update the hero flags
				enemies.update(hero, game_settings.enemy_speed)
				tick += 1
				if tick % 50 == 0:
					enemies.add(Enemy(screen, game_settings))
				bullets.update() #call the update method in the while loop
				
				for enemy in enemies:
					for bullet in bullets: # get rid of bullets that are off the screen
						if bullet.rect.bottom <= 0: #bullet bottom is at the top of the screen
							bullets.remove(bullet) #call remove()
						if len(bullets) >= 10:
							bullets.remove(bullet)
						if enemy.rect.colliderect(bullet.rect):
							count += 1
							count_update = "Enemies Killed: %d" %count
							scoreboard = Scoreboard(screen, count_update)
							
							enemies.remove(enemy)
							bullets.remove(bullet)
							pygame.mixer.music.load('sounds/win.wav')
							pygame.mixer.music.play(0)
					if enemy.rect.colliderect(hero.rect):
						print "The monster got you! You died!"
						pygame.mixer.music.load('sounds/lose.wav')
						pygame.mixer.music.play(0)
```

Code for enemy that spawns randomly at the top of the screen and moves towards the hero
```python
	class Enemy(Sprite):
	def __init__(self, screen, game_settings):
		super(Enemy, self).__init__()
		self.screen = screen

		self.enemy_image = pygame.image.load('images/monster1.png')
		self.rect = self.enemy_image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = randint(self.screen_rect.left, self.screen_rect.right)
		self.rect.top = self.screen_rect.top

	def update(self, hero, speed = 3):
		dx, dy = self.rect.x - hero.rect.x, self.rect.y - hero.rect.y
		dist = math.hypot(dx, dy)
		dx, dy = dx / dist, dy / dist

		self.rect.x -= dx * speed
		self.rect.y -= dy * speed

	def draw_enemy(self):
		self.screen.blit(source = self.enemy_image, dest = self.rect)

	def __exit__(self, *err):
		self.remove(self)
```		