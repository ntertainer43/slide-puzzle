import pygame, sys
from pygame.locals import  *
import random

class Puzzle_box:
    def __init__(self, num, x, y):
        self.position = (x,y)
        self.num = num
        self.animate = False


    def display(self): #To DO REMAINING MAKE A WAY TO ANIMATE THE SLIDING OF THE TILE
        pygame.draw.rect(SURFACE, TILECOLOR, (self.position[0]*100, self.position[1]*100, 100, 100))
        textSurf = FONT.render(str(self.num), True, (255,255,255))
        textRect = textSurf.get_rect()
        textRect.center = self.position[0]*100 +50, self.position[1]*100 +50
        SURFACE.blit(textSurf, textRect)


    def pos_update(self, last):
        if self.position == (blankx, blanky):
            self.position = last




def main():
    global SURFACE, FONT, TILECOLOR, BGCOLOR, blankx, blanky, last

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SURFACE = pygame.display.set_mode((600,600))
    pygame.display.set_caption('Slide Puzzle')
    FONT = pygame.font.Font('freesansbold.ttf', 20)
    num = 1
    BGCOLOR = (3, 54,73)
    TILECOLOR = (0, 204, 0)
    list_of_boxes = []
    list_of_position= []
    for i in range (1,5):
        for j in range(1,5):
            list_of_position.append((j,i))
            if num == 16:
                break
            new_Box = Puzzle_box(num, j,i)
            list_of_boxes.append(new_Box)
            num+=1
    random.shuffle(list_of_position)
    blankx, blanky = list_of_position[0]
    last = blankx, blanky


    for box in list_of_boxes:
        box.position = list_of_position[num-1]
        num -=1


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:  #CHANGE THIS PART TO FIT YOUR CODE
                if event.key in (K_LEFT, K_a) and isValidMove(blankx, blanky, "LEFT"):
                    blankx +=1


                elif event.key in (K_RIGHT, K_d) and isValidMove(blankx, blanky, 'RIGHT'):
                    blankx -=1


                elif event.key in (K_UP, K_w) and isValidMove(blankx, blanky,"UP"):
                    blanky +=1

                elif event.key in (K_DOWN,K_s) and isValidMove(blankx, blanky, "DOWN"):
                    blanky -=1



        SURFACE.fill(BGCOLOR)
        for new_Box in list_of_boxes:
            new_Box.pos_update(last)
            new_Box.display()
        win = gamewin(list_of_boxes)
        gamewinAnimation(win)
        print(win)
        pygame.display.update()

        last = (blankx, blanky)
        FPSCLOCK.tick(15)


def isValidMove(blankx, blanky, dire):
    if blankx== 4 and dire =='LEFT':
        return False
    elif blankx == 1 and dire =="RIGHT":
        return  False
    elif blanky == 4 and dire =="UP":
        return False
    elif blanky == 1 and dire =="DOWN":
        return  False
    else:
        return True

def gamewin(list_of_boxes):
    game_state= [ boxes.position for boxes in list_of_boxes]
    game_state.append((4,4))
    wingame = []
    for i in range(1,5):
        for j in range(1,5):

            wingame.append((j,i))
    if game_state == wingame:
        return True

    return False


def gamewinAnimation(win):
    if win == True:

        FONT2 = pygame.font.Font('freesansbold.ttf', 40)
        textwin = FONT2.render(str('You have won the game'), True, (255, 200, 100))
        textwinRect = textwin.get_rect()
        textwinRect.center = 300, 300
        SURFACE.blit(textwin, textwinRect)



if __name__ == '__main__':
    main()
