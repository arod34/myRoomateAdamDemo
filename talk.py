import pygame
dialogue = [
        ["blah blah blah", "you suck", "i hate you"],
        ["stinky face", "go blues"],
        ["i am programmer", "brokie brian"],
        ["athens here i come", "gyro's from arbys are my favorite antonio says", "brian sucks at mario kart"]
        ]



# talking to adam class
class talk:

    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)
        self.cooldown = 0

    def checkForClick(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.cooldown <= 0:
                self.cooldown = 30
                return 1
        return 0
    
    def continueDialogue(self, index1, index2):
        return dialogue[index1][index2]
    
    def updateIndex(self, index1, index2):
        if index2 < len(dialogue[index1])-1:
            return index1, index2+1
        if index1 < len(dialogue)-1:
            index2 = 0
            return index1+1, index2
        return 0,0
    
    def stopTalking(self, index1, index2):
        if index1 == 0 and index2 == 0:
            return len(dialogue)-1, len(dialogue[index1])-1
        if index2 == 0 and index1 != 0:
            return index1-1, len(dialogue[index1-1])-1
        return index1, index2-1
    
    def display_text(surface, text, pos, font, color):
        collection = [word.split(' ') for word in text.splitlines()]
        space = font.size(' ')[0]
        x,y = pos
        for lines in collection:
            for words in lines:
                word_surface = font.render(words, True, color)
                word_width , word_height = word_surface.get_size()
                if x + word_width >= 800:
                    x = pos[0]
                    y += word_height
                surface.blit(word_surface, (x,y))
                x += word_width + space
            x = pos[0]
            y += word_height

    