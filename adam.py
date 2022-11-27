import pygame 
from imageLoading import adamClosed, adamOpened
class adam:

    def __init__(self, image, x, y):
        self.x = x
        self.y = y
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width // 2), int(height // 2)))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        self.cooldown = 10
        self.open = False

    def updateAdam(self):
        if self.cooldown == 0:
            if self.open:
                self.image = self.shrink(adamClosed)
                self.open = False
                self.cooldown = 10
            else:
                self.image = self.shrink(adamOpened)
                self.open = True
                self.cooldown = 10
        
    def shrink(self, image):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width // 2), int(height // 2)))
        return self.image