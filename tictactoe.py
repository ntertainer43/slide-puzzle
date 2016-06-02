import pygame, sys
from pygame.locals import *
import random

class AI:
    def __init__(self, level,list_of_boxes ):
        self.level = level
        self.list = list_of_boxes


    def  ThreeInARow(self):
        for box in self.list:
            print("nimesh")



class Box:
    def __init__(self , x,y):
        self.value = 0
        self.position= (x,y)


    def display(self ):
        if self.value == 1:
            pygame.draw.line(SURFACE, LINECOLOR, (self.position[0]*100+25, self.position[1]*100+ 25),((self.position[0]+1)*100-25,(self.position[1]+1)*100-25))
            pygame.draw.line(SURFACE, LINECOLOR, (self.position[0]*100+25, (self.position[1]+1)*100- 25),((self.position[0]+1)*100-25 ,self.position[1]*100+25))
        elif self.value == -1:
            pygame.draw.circle(SURFACE, LINECOLOR, (self.position[0]*100+50,self.position[1]*100+50), 25)

    def update(self, player, event):
        vol = pygame.draw.rect(SURFACE, BGCOLOR, (self.position[0]*100, self.position[1]*100,95,95))
        if self.value !=0:      # check if there is any sign on the box and prevent it from getting changed
            return player
        if player == 1:
            if vol.collidepoint(event.pos[0], event.pos[1]):
                self.value = 1
                return player *-1
        elif player == -1:
            if vol.collidepoint(event.pos[0], event.pos[1]):
                self.value = -1
                return player *-1
        return player




def main():
    global SURFACE, LINECOLOR, BGCOLOR, WIN

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SURFACE = pygame.display.set_mode((600,600))
    pygame.display.set_caption('Tic tac Toe')
    FONT = pygame.font.Font('freesansbold.ttf', 20)
    WIN = [(1,2,3),(1,4,7),(2,5,8), (3,6,9),(4,5,6), (7,8,9), (1,5,9),(7,5,3)]
    player = 1
    BGCOLOR = (83, 54,73)
    LINECOLOR = (0, 0, 0)
    list_of_boxes = []
    for i in range(1,4):
        for j in range(1,4):
            new_box = Box(j,i)
            list_of_boxes.append(new_box)

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                for box in list_of_boxes:
                   player = box.update(player,event)

        SURFACE.fill(BGCOLOR)
        for box in list_of_boxes:
            box.display()
        drawlines()
        hasWon(list_of_boxes)
        pygame.display.update()
        FPSCLOCK.tick(.5)


def drawlines():
    pygame.draw.line(SURFACE,LINECOLOR,  (200,100), (200,400))
    pygame.draw.line(SURFACE,LINECOLOR,  (300,100), (300,400))
    pygame.draw.line(SURFACE,LINECOLOR,  (100,200), (400,200))
    pygame.draw.line(SURFACE,LINECOLOR,  (100,300), (400,300))

def hasWon(list_of_boxes):
    box_pos = []
    i = 1
    player1 =[]
    player2 =[]
    for box in list_of_boxes:
        box_pos.append([box.value,i])
        i+=1

    for mark, ind in box_pos:
        if mark == 1:
            player1.append(ind)
        elif mark == -1:
            player2.append(ind)
    print(player1)
    for permu in WIN:
        
        if permu == player1:
            print("Player1 has won")
        
    
                
    


if __name__ == '__main__':
    main()
