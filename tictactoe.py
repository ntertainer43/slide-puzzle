import pygame, sys
from pygame.locals import *
import random

class AI:
    def __init__(self, level,list_of_boxes ):
        self.level = level
        self.list = list_of_boxes
        self.opp= []


    def move(self):
        valid_moves =[]
        valid_boxes = []
        for box in self.list:
            if box.value == 0:

                valid_moves.append((box,(box.position[0])+ (box.position[1]-1)*3))
        if self.level == "medium":
            self.smart_move(valid_moves)
        random.shuffle(valid_moves)
        random.shuffle
        valid_moves[-1][0].value = -1
        valid_moves.pop()
        print(valid_moves)
        pygame.time.wait(300)
        return 1

    def smart_move(self, valid_moves):

        for permu in WIN:
            wise_move = set(permu)-set(self.opp)
            print(set(permu),set(self.opp), wise_move, len(wise_move))
            if (len(wise_move)== 1 or len(wise_move)== 2) and wise_move < set(valid_moves):
               ind = wise_move.pop()
               print("got into wise mode")
               valid_boxes[ind].value = -1



    def hasWon(self, list_of_boxes):
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
        self.opp = player1
        for permu in WIN:
            if set(permu) <set(player1) or set(permu)== set(player1):
                gameWinAnimation("Player 1")
                return False
            elif set(permu) <set(player2) or set(permu) == set(player2):
                gameWinAnimation("Comp")
                return False
        return True



class Box:
    def __init__(self , x,y):
        self.value = 0
        self.position= (x,y)


    def display(self ):
        if self.value == 1:
            pygame.draw.line(SURFACE, LINECOLOR, (self.position[0]*100+25, self.position[1]*100+ 25),((self.position[0]+1)*100-25,(self.position[1]+1)*100-25),5)
            pygame.draw.line(SURFACE, LINECOLOR, (self.position[0]*100+25, (self.position[1]+1)*100- 25),((self.position[0]+1)*100-25 ,self.position[1]*100+25),5)
        elif self.value == -1:
            pygame.draw.circle(SURFACE, LINECOLOR, (self.position[0]*100+50,self.position[1]*100+50), 25,5)

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
    global SURFACE, LINECOLOR, BGCOLOR, WIN, FONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SURFACE = pygame.display.set_mode((550,500))
    pygame.display.set_caption('Tic tac Toe')
    FONT = pygame.font.Font('freesansbold.ttf', 20)
    WIN = [[1,2,3],[1,4,7],[2,5,8], [3,6,9],[4,5,6], [7,8,9], [1,5,9],[7,5,3]]
    player = -1  #Player state can be 1 for player 1 and -1 for player 2
    BGCOLOR = (83, 54,73)
    LINECOLOR = (0, 0, 0)
    NotWin = True
    
    list_of_boxes = []
    for i in range(1,4):
        for j in range(1,4):
            new_box = Box(j,i)
            list_of_boxes.append(new_box)
    random_bot = AI("medium", list_of_boxes)
    while True:
        #event handling loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP and NotWin == True and player == 1:

                for box in list_of_boxes:
                #keeps track of players when valid mouse button is pressed
                   player = box.update(player,event)

        SURFACE.fill(BGCOLOR)
        drawlines()
        if player == -1 and NotWin:
            player =random_bot.move()
        NotWin = random_bot.hasWon(list_of_boxes)
        for box in list_of_boxes:
            box.display()

        reset()

        pygame.display.update()
        FPSCLOCK.tick(30)


def drawlines():
    pygame.draw.line(SURFACE,LINECOLOR,  (200,100), (200,400),5)
    pygame.draw.line(SURFACE,LINECOLOR,  (300,100), (300,400),5)
    pygame.draw.line(SURFACE,LINECOLOR,  (100,200), (400,200),5)
    pygame.draw.line(SURFACE,LINECOLOR,  (100,300), (400,300),5)


    
                
def gameWinAnimation(Player):
    FONT2 = pygame.font.Font('freesansbold.ttf', 40)
    textwin = FONT2.render(str(Player +' Has won the game'), True, (255, 200, 100))
    textwinRect = textwin.get_rect()
    textwinRect.center = 270, 300
    SURFACE.blit(textwin, textwinRect)

def reset():
    resettext = FONT.render(str('Reset'), True, (45,34,100))
    resetrect = resettext.get_rect()
    resetrect.center = 120,50
    
    SURFACE.blit(resettext, resetrect)


if __name__ == '__main__':
    main()
