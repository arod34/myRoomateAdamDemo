import pygame

# progressing day class
class sleep:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)