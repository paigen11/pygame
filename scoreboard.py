import pygame.font

class Scoreboard(object):
	def __init__(self, screen, scoreboard_text, enemy_count):
		self.screen = screen
		self.screen_rect = screen.get_rect()

		self.width = 200
		self.height = 150
		self.scoreboard_color = 230, 153, 255
		self.text_color = 255,255,255
		self.font = pygame.font.Font(None, 40)
		self.rect = pygame.Rect(0,0, self.width, self.height)
		self.rect.centerx = self.screen_rect.centerx
		self.rect.top = self.screen_rect.top
		self.scoreboard_message(scoreboard_text)

	def scoreboard_message(self, scoreboard_text):
		self.image_message = self.font.render(scoreboard_text, True, self.text_color)
		self.image_message_rect = self.image_message.get_rect()
		self.image_message_rect.center = self.rect.center

	def draw_scoreboard(self):
		self.screen.fill(self.scoreboard_color, self.rect)
		self.screen.blit(self.image_message, self.image_message_rect)		