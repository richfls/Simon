import pygame
import random
import winsound
pygame.init()#initializes Pygame
pygame.display.set_caption("Simon!")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen

#game variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers in a TUPLE
turn = False
pattern = [] #this holds the random pattern
pi = 3.1415

R = (155, 0, 0)


class simon:
    def __init__(self, xpos, ypos,angle1, angle2, color):
        self.xpos = xpos
        self.ypos = ypos
        self.angle1 = angle1
        self.angle2 = angle2
        self.color = color
        self.light = False
        self.y = (155,155,0)
    def draw(self):
        if light == True:
            yellow += (100,100,0)
        else:
            pass

        pygame.draw.arc(screen, color, (200,200,400,400), angle1, angle2, 100)
    def drawlight(self):
        pass


#more colors go here!   
pygame.display.flip()

#gameloop###################################################
while True:

    event = pygame.event.wait()#event queue 

    #input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        turn = True

    if event.type == pygame.MOUSEBUTTONUP:
        turn = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
    #update section---------------------------------------------
    if turn == True:
        pattern.append(random.randrange(0, 4)) #push a new value into the pattern list

        #brighten colors and play beep for each number in the pattern
        for i in range(len(pattern)): 
            if pattern[i]==0: #RED
                pygame.draw.arc(screen, (R), (200,200,400,400), pi/2, pi, 100)
                pygame.display.flip()
                winsound.Beep(440, 500)

            elif pattern[i]==1:#GREEN
                pygame.draw.arc(screen, (0, 255, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
                pygame.display.flip()
                winsound.Beep(640, 500)

            elif pattern[i]==2:#Y
                pygame.draw.arc(screen, (255, 255, 0), (200, 200, 400, 400), (3*pi/2), 0, 100)
                pygame.display.flip()
                winsound.Beep(840, 500)

            elif pattern[i]==3:#b
                pygame.draw.arc(screen, (0, 0, 255), (200, 200, 400, 400), 0, pi/2, 100)
                pygame.display.flip()
                winsound.Beep(330, 500)
            #redraw board after every beep
            pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
            pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
            pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), (3*pi/2), 0, 100)
            pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), 0, pi/2, 100)
            pygame.display.flip()
            pygame.time.wait(200) #slows the game down a bit

    turn = False       
    #render section---------------------------------------------

    #game board
    pygame.draw.arc(screen, (155, 0,0), (200,200,400,400), pi/2, pi, 100)
    pygame.draw.arc(screen, (0, 155, 0), (200, 200, 400, 400), pi, (3*pi/2), 100)
    pygame.draw.arc(screen, (155, 155, 0), (200, 200, 400, 400), (3*pi/2), 0, 100)
    pygame.draw.arc(screen, (0, 0, 155), (200, 200, 400, 400), 0, pi/2, 100)
    #more colors go here!

    pygame.display.flip()


#end game loop##############################################

pygame.quit()
