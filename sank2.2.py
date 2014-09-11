#!c:\python24\python.exe
import random,math,pygame
from pygame.locals import *

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
ARROW = DOWN
WINSIZE = [640, 480]
WIDTH = 16
HEIGHT = 16
SNAKBODY = [(10,3),(10,2),(10,1)]
FOOD = [(20,25)]
BLACK = 20, 20, 40
RED = 255, 0, 0
CONTER = 0
Font = None
GAMEOVER = False

def showtext(surface, pos, text, color, bgcolor):
    textimg = Font.render(text, 1, color, bgcolor)
    surface.blit(textimg, pos)
    return pos[0] + textimg.get_width()

def draw(surface):
    surface.fill(BLACK)
    for x, y in SNAKBODY:
        rect = x*WIDTH, y*HEIGHT, WIDTH, HEIGHT
        pygame.draw.rect(surface, RED, rect)
    for x, y in FOOD:
        rect = x*WIDTH, y*HEIGHT, WIDTH, HEIGHT
        pygame.draw.rect(surface, RED, rect)
    showtext(surface, (20,20), 'You Get '+str(CONTER)+' $', RED, BLACK)
    if CONTER >= 2000:
        showtext(surface, (20,60), 'Good!', RED, BLACK)
    if CONTER >= 3000:
        showtext(surface, (20,60), 'Best!!', RED, BLACK)
    if GAMEOVER == True:
        showtext(surface, (270,200), 'Game Over !', RED, BLACK)

def makebody(surface):
    global ARROW,CONTER
    (x,y) = SNAKBODY[0]
    if ARROW == UP:
        y = y-1
    elif ARROW == DOWN:
        y = y+1
    elif ARROW == LEFT:
        x = x-1
    elif ARROW == RIGHT:
        x = x+1
    x = x%40
    y = y%30
    global GAMEOVER
    for x1, y1 in SNAKBODY:
        if x1 == x and y1 == y:
            pygame.time.set_timer(USEREVENT, 0)
            GAMEOVER = True
    SNAKBODY.insert(0, (x,y))
    for x1, y1 in FOOD:
        if x1 == x and y1 == y:
            FOOD[0] = (random.randrange(40), random.randrange(30))
            CONTER += 100
            if CONTER == 1000:
                pygame.time.set_timer(USEREVENT, 30)
            if CONTER == 2000:
                pygame.time.set_timer(USEREVENT, 20)
            if CONTER == 3000:
                pygame.time.set_timer(USEREVENT, 10)
        else:
            SNAKBODY.pop()


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('snak2')
    pygame.time.set_timer(USEREVENT, 50)
    done = True
    global Font
    Font = pygame.font.Font(None, 26)	
    while done:
        draw(screen)
        pygame.display.update()
        global ARROW
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_q):
                done = False
                break
            elif e.type == KEYDOWN and e.key == K_UP and ARROW <> DOWN:
                ARROW = UP
            elif e.type == KEYDOWN and e.key == K_DOWN and ARROW <> UP:
                ARROW = DOWN
            elif e.type == KEYDOWN and e.key == K_LEFT and ARROW <> RIGHT:
                ARROW = 2
            elif e.type == KEYDOWN and e.key == K_RIGHT and ARROW <> LEFT:
                ARROW = 3
            elif e.type == USEREVENT:
                makebody(screen)

if __name__ == '__main__':
    main()
