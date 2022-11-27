import pygame

SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920 
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


# loading images into variables
quitButton = pygame.image.load("pictures/quitButton.png").convert_alpha()
sleepButton = pygame.image.load("pictures/sleepButton.png").convert_alpha()
talkButton = pygame.image.load("pictures/talkButton.png").convert_alpha()
background = pygame.image.load("pictures/adam_bedroom.jpg").convert_alpha()
adamClosed = pygame.image.load("pictures/adamClosed.png").convert_alpha()
adamOpened = pygame.image.load("pictures/adamOpen.png").convert_alpha()
textbox = pygame.image.load("pictures/textBox.png").convert_alpha()
title = pygame.image.load("pictures/title.png").convert_alpha()
titleBackground = pygame.image.load("pictures/adamTitle.jpg").convert_alpha()
playButton = pygame.image.load("pictures/play.png").convert_alpha()
quitButton2 = pygame.image.load("pictures/quit.png").convert_alpha()
heart = pygame.image.load("pictures/heart.png").convert_alpha()