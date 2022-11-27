import pygame
#from main import screen

class Buttons:
    def __init__(self, x, y, image, scale) -> None:
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width // scale), int(height // scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    

    def checkClick(self):
        action = False
        pos = pygame.mouse.get_pos()

     

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
               

        
        
        return action
    
   


#if quit_button.draw():
 #       run = False
  #  if sleep_button.draw():
   #     screen.fill((255,255,255))
    #if talk_button.draw():
     #   if text_on_screen == False:
      #      text_on_screen = True
       #     t.message = font.render("LLLL",True,(255,255,255))
        #    screen.blit(background,(0,0))
         #   talk.stop()
          #  talk2.play()
        #else:
            
         #  text_on_screen = False
          #  t.message = font.render("hhhh",True,(255,255,255))
          #  screen.blit(background,(0,0))
          #  talk2.stop()
           # talk.play()
    
    #if text_on_screen == True:
    #t.draw_text()

    #if adam.cooldown == 0:
     #   if opened == True:
      #      screen.blit(background,(0,0))
       #     adam.draw_adam(SCREEN_WIDTH//2,SCREEN_HEIGHT//2,adamClosed,2)
        #    opened = False
        #else:
         #   screen.blit(background,(0,0))
          #  adam.draw_adam(SCREEN_WIDTH//2,SCREEN_HEIGHT//2,adamOpened,2)
           # opened = True
        #adam.cooldown = 10
               