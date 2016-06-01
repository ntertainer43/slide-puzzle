import pygame, sys
from pygame.locals import  *

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
        print( self.num , textRect.center)


def main():
    global SURFACE, FONT, TILECOLOR

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SURFACE = pygame.display.set_mode((600,600))
    pygame.display.set_caption('Slide Puzzle')
    FONT = pygame.font.Font('freesansbold.ttf', 20)
    num = 1
    BGCOLOR = (3, 54,73)
    TILECOLOR = (0, 204, 0)
    list_of_boxes = []
    for i in range (1,5):
        for j in range(1,5):
           if num == 16:
               break
           new_Box = Puzzle_box(num, j,i)
           list_of_boxes.append(new_Box)
           num+=1
    blankx, blanky = 4,4

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:  #CHANGE THIS PART TO FIT YOUR CODE
                if event.key in (K_LEFT, K_a) and isValidMove(blankx, blanky, "LEFT"):
                    blankx +=1
                    list_of_boxes[(blanky-1)*4+blankx-1].position= (blankx-1, blanky)
                elif event.key in (K_RIGHT, K_d) and isValidMove(blankx, blanky, 'RIGHT'):
                    blankx -=1
                    list_of_boxes[(blanky-1)*4+blankx-1].position= (blankx +1, blanky)

                elif event.key in (K_UP, K_w) and isValidMove(blankx, blanky,"UP"):
                    blanky +=1
                    list_of_boxes[(blanky-1)*4+blankx-1].position= (blankx, blanky-1)

                elif event.key in (K_DOWN,K_s) and isValidMove(blankx, blanky, "DOWN"):
                    blanky -=1
                    list_of_boxes[(blanky-1)*4+blankx-1].position= (blankx, blanky+1)

        SURFACE.fill(BGCOLOR)
        for new_Box in list_of_boxes:
            new_Box.display()
        pygame.display.update()
        print(blankx, blanky)
        FPSCLOCK.tick(30)


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


if __name__ == '__main__':
    main()
