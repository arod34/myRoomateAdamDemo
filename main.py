import pygame , sys 
from pygame import mixer
from button import Buttons
from talk import talk
from sleep import sleep
from leave import leave
from imageLoading import quitButton, sleepButton, talkButton, background, adamClosed, adamOpened, textbox, screen, title, titleBackground, heart, playButton, quitButton2
from adam import adam
print(pygame.__version__)

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 60)

def update_fps():
    fps = str(int(clock.get_fps()))
    print(fps)
    fps_text = font.render(fps,1,(255,255,255))
    return fps_text


vocals = [
        [mixer.Sound("audio/dialogue00.wav"),mixer.Sound("audio/dialogue01.wav"),mixer.Sound("audio/dialogue02.wav")],
        [mixer.Sound("audio/dialogue10.wav"),mixer.Sound("audio/dialogue11.wav")],
        [mixer.Sound("audio/dialogue20.wav"),mixer.Sound("audio/dialogue21.wav")],
        [mixer.Sound("audio/dialogue30.wav"),mixer.Sound("audio/dialogue31.wav"),mixer.Sound("audio/dialogue32.wav")]
        ]

win = mixer.Sound("audio/dialogueWin.wav")

# ----------------- create window -----------------


pygame.display.set_caption('DEMO')

# ----------------- text window -------------------


class Text:

    def __init__(self, color, message):
        self.color = color
        self.message = font.render(message,True, color)

    def changeText(self, message):
        self.message = font.render(message, True, self.color)

    def displayText(self):
        screen.blit(self.message, (60,75))

# ----------------- Game Loop ---------------------
run = True
speak = talk(talkButton, 1600, 150)
bedtime = sleep(sleepButton, 1600, 400)
done = leave(quitButton, 1600, 650)
Adam = adam(adamClosed,190,-200)

t = Text((255,255,255),"poopy Face")
index1_count = 0
index2_count = 0
index1_talk = 0
index2_talk = 0
t.changeText(speak.continueDialogue(index1_count,index2_count))
dialogue_done = index1_count
speaking = False
completion = 0

run2 = True
screen.blit(titleBackground,(0,0))
screen.blit(title,(200,0))
play = Buttons(860,700,playButton,1)
quity = Buttons(860, 900, quitButton2, 1)
screen.blit(play.image,(play.rect.x,play.rect.y))
screen.blit(quity.image,(quity.rect.x,quity.rect.y))
run3 = True
while run:
    if play.checkClick():
        run = False

    if quity.checkClick():
        run = False
        run2 = False
        run3 = False

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(60)
    pygame.display.update()
    #if quity.checkClick():
     #   run = False
      #  run2 = False

 
screen.blit(background,(0,0))
screen.blit(speak.image,(speak.x,speak.y))
screen.blit(bedtime.image,(bedtime.x,bedtime.y))
screen.blit(done.image,(done.x,done.y))
screen.blit(Adam.image,(Adam.x,Adam.y))
#run = True
while run3:
    

    if speaking:
        Adam.updateAdam()
        screen.blit(Adam.image,(Adam.x,Adam.y))

    else:
        Adam.image = Adam.shrink(adamClosed)
        #screen.blit(Adam.image, (Adam.x,Adam.y))
        

    done.checkForClick()
    if speak.checkForClick() == 1: 
        index1_talk, index2_talk = speak.stopTalking(index1_count, index2_count)
        vocals[index1_talk][index2_talk].stop()
        screen.blit(textbox, (25,50))
        
        
        screen.blit(background,(0,0))
        screen.blit(Adam.image,(Adam.x,Adam.y))
        screen.blit(speak.image,(speak.x,speak.y))
        screen.blit(bedtime.image,(bedtime.x,bedtime.y))
        screen.blit(done.image,(done.x,done.y))
        screen.blit(font.render("Talk to Adam 50 times. currently spoken: "+str(completion),1,(255,255,255)),(0,0))
        if (dialogue_done == index1_count):
            screen.blit(textbox, (25,50))
            t.displayText()
            
            vocals[index1_count][index2_count].play()
            index1_count, index2_count = speak.updateIndex(index1_count, index2_count)
            t.changeText(speak.continueDialogue(index1_count,index2_count))
            speaking = True
        else:
            dialogue_done = index1_count
            speaking = False

        completion += 1

    if completion == 50:
        run3 = False
            
    
    
    update_fps()
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if speak.cooldown > 0:
        speak.cooldown -= 1

    if Adam.cooldown > 0:
        Adam.cooldown -= 1
    clock.tick(60)
    pygame.display.update()



screen.blit(titleBackground,(0,0))
done2 = leave(quitButton2, 880,540)
screen.blit(done2.image, (880,540))
t.changeText("Adam Loves you now!!!! congrats you win!!!!")
screen.blit(t.message,(500,200))
while run2:
    
    done2.checkForClick()
    win.play()

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run3 = False

    clock.tick(60)
    pygame.display.update()
        
pygame.quit()
sys.exit()