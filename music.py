import pygame

pygame.mixer.init()
win_sound = pygame.mixer.Sound('sounds/win3.wav')
lose_sound = pygame.mixer.Sound('sounds/lose.wav')
lose_sound.play()
while True:
    pass

pygame.mixer.quit()
