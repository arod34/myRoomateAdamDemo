import pygame, sys

# quitting game class
class leave:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)

    def checkForClick(self):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                pygame.quit()
                sys.exit()