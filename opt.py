import sys
from math import sqrt
from random import randint
import pygame
 
pygame.init()
smallfont = pygame.font.SysFont(None, 36)
largefont = pygame.font.SysFont(None, 72)
 
BLACK = (0,0,0)
pygame.key.set_repeat(30, 30)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

WIDTH = 12
HEIGHT = 22
INTERVAL = 40
FIELD = []
COLORS = ((0, 0, 0), (255, 165, 0), (0, 0, 255), (0, 255, 255), \
          (0, 255, 0), (255, 0, 255), (255, 255, 0), (255, 0, 0), (128, 128, 128))

BLOCK = None
NEXT_BLOCK = None
PIECE_SIZE = 24
PIECE_GRID_SIZE = PIECE_SIZE+1 

BLOCK_DATA = (
    (
        (0, 0, 1, \
         1, 1, 1, \
         0, 0, 0),
        (0, 1, 0, \
         0, 1, 0, \
         0, 1, 1),
        (0, 0, 0, \
         1, 1, 1, \
         1, 0, 0),
        (1, 1, 0, \
         0, 1, 0, \
         0, 1, 0),
    ), (
        (2, 0, 0, \
         2, 2, 2, \
         0, 0, 0),
        (0, 2, 2, \
         0, 2, 0, \
         0, 2, 0),
        (0, 0, 0, \
         2, 2, 2, \
         0, 0, 2),
        (0, 2, 0, \
         0, 2, 0, \
         2, 2, 0)
    ), (
        (0, 3, 0, \
         3, 3, 3, \
         0, 0, 0),
        (0, 3, 0, \
         0, 3, 3, \
         0, 3, 0),
        (0, 0, 0, \
         3, 3, 3, \
         0, 3, 0),
        (0, 3, 0, \
         3, 3, 0, \
         0, 3, 0)
    ), (
        (4, 4, 0, \
         0, 4, 4, \
         0, 0, 0),
        (0, 0, 4, \
         0, 4, 4, \
         0, 4, 0),
        (0, 0, 0, \
         4, 4, 0, \
         0, 4, 4),
        (0, 4, 0, \
         4, 4, 0, \
         4, 0, 0)
    ), (
        (0, 5, 5, \
         5, 5, 0, \
         0, 0, 0),
        (0, 5, 0, \
         0, 5, 5, \
         0, 0, 5),
        (0, 0, 0, \
         0, 5, 5, \
         5, 5, 0),
        (5, 0, 0, \
         5, 5, 0, \
         0, 5, 0)
    ), (
        (6, 6, \
        6, 6),
        (6, 6, \
        6, 6),
        (6, 6, \
        6, 6),
        (6, 6, \
        6, 6)
    ), (
        (0, 7, 0, 0, \
         0, 7, 0, 0, \
         0, 7, 0, 0, \
         0, 7, 0, 0),
        (0, 0, 0, 0, \
         7, 7, 7, 7, \
         0, 0, 0, 0, \
         0, 0, 0, 0),
        (0, 0, 7, 0, \
         0, 0, 7, 0, \
         0, 0, 7, 0, \
         0, 0, 7, 0),
        (0, 0, 0, 0, \
         0, 0, 0, 0, \
         7, 7, 7, 7, \
         0, 0, 0, 0)
    )
)

class Block:
    """ 블록 객체 """
    def __init__(self, count):
        self.turn = randint(0,3)
        self.type = BLOCK_DATA[randint(0, 6)]
        self.data = self.type[self.turn]
        self.size = int(sqrt(len(self.data)))
        self.xpos = randint(2, 8 - self.size)
        self.ypos = 1 - self.size
        self.fire = count + INTERVAL
 
    def update(self, count):
        """ 블록 상태 갱신 (소거한 단의 수를 반환한다) """
        erased = 0
        if is_overlapped(self.xpos, self.ypos + 1, self.turn):
            for y_offset in range(BLOCK.size):
                for x_offset in range(BLOCK.size):
                    index = y_offset * self.size + x_offset
                    val = BLOCK.data[index]
                    if 0 <= self.ypos+y_offset < HEIGHT and \
                       0 <= self.xpos+x_offset < WIDTH and val != 0:
                            FIELD[self.ypos+y_offset][self.xpos+x_offset] = val
 
            erased = erase_line()
            go_next_block(count)
 
        if self.fire < count:
            self.fire = count + INTERVAL
            self.ypos += 1
        return erased
 
    def draw(self):
        for y_offset in range(self.size):
            for x_offset in range(self.size):
                index = y_offset * self.size + x_offset
                val = self.data[index]
                if 0 <= y_offset + self.ypos < HEIGHT and \
                   0 <= x_offset + self.xpos < WIDTH and val != 0:
                    f_xpos = PIECE_GRID_SIZE + (x_offset + self.xpos) * PIECE_GRID_SIZE
                    f_ypos = PIECE_GRID_SIZE + (y_offset + self.ypos) * PIECE_GRID_SIZE
                    pygame.draw.rect(screen, COLORS[val],
                                    (f_xpos, 
                                    f_ypos, 
                                    PIECE_SIZE, 
                                    PIECE_SIZE))
 
def erase_line():
    erased = 0
    return erased
 
def is_game_over():
    pass
 
def go_next_block(count):
    global BLOCK, NEXT_BLOCK
    BLOCK = NEXT_BLOCK if NEXT_BLOCK != None else Block(count)
    NEXT_BLOCK = Block(count)
 
def is_overlapped(xpos, ypos, turn):
    data = BLOCK.type[turn]
    for y_offset in range(BLOCK.size):
        for x_offset in range(BLOCK.size):
            index = y_offset * BLOCK.size + x_offset
            val = data[index]

            if 0 <= xpos+x_offset < WIDTH and \
                0 <= ypos+y_offset < HEIGHT:
                if val != 0 and \
                    FIELD[ypos+y_offset][xpos+x_offset] != 0:
                    return True
    return False

def set_game_field():
    for i in range(HEIGHT-1):
        FIELD.insert(0, [8, 0,0,0,0,0,0,0,0,0,0 ,8])
    
    FIELD.insert(HEIGHT-1, [8, 8,8,8,8,8,8,8,8,8,8 ,8])
    
    
def draw_game_field():
    for y_offset in range(HEIGHT):
        for x_offset in range(WIDTH):
            val = FIELD[y_offset][x_offset]
            color = COLORS[val]
            pygame.draw.rect(screen, 
                            color,
                            (PIECE_GRID_SIZE + x_offset*PIECE_GRID_SIZE, 
                            PIECE_GRID_SIZE + y_offset*PIECE_GRID_SIZE , 
                            PIECE_SIZE , 
                            PIECE_SIZE ))
    #pass


def draw_current_block():
    BLOCK.draw()

def draw_next_block():
    for y_offset in range(NEXT_BLOCK.size):
        for x_offset in range(NEXT_BLOCK.size):
            index = y_offset * NEXT_BLOCK.size + x_offset
            val = NEXT_BLOCK.data[index]
            if val != 0:
                f_xpos = 460 + (x_offset) * PIECE_GRID_SIZE
                f_ypos = 100 + (y_offset) * PIECE_GRID_SIZE
                pygame.draw.rect(screen, COLORS[val],
                                (f_xpos, 
                                f_ypos, 
                                PIECE_SIZE, 
                                PIECE_SIZE))
 
def draw_score(score):
    score_str = str(score).zfill(6)
    score_image = smallfont.render(score_str, True, (0, 255, 0))
    screen.blit(score_image, (500, 30))
    
def erase_line():
    erased = 0
    ypos = HEIGHT-2
    print(FIELD[ypos])
    while ypos >=0:
        if  all(FIELD[ypos]) == True:
            del FIELD[ypos]
            FIELD.insert(0, [8, 0,0,0,0,0,0,0,0,0,0 ,8])
            erased += 1
        else:
            ypos -= 1
    return erased
 
def draw_gameover_message():
    score_image = smallfont.render( 'game_over', True, (0, 255, 0))
    pass
 
def runGame():
    global INTERVAL
    count = 0
    score = 0
    game_over = False
    
    go_next_block(INTERVAL)
 
    set_game_field()
 
    while True:
        clock.tick(10)
        screen.fill(BLACK)
 
        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = event.key
            elif event.type == pygame.KEYUP:
                key = None
 
        game_over = is_game_over()
        if not game_over:
            count += 5
            if count % 1000 == 0:
                INTERVAL = max(1, INTERVAL - 2)
            erased = BLOCK.update(count)
 
            if erased > 0:
                score += (2 ** erased) * 100
 
            # 키 이벤트 처리
            next_x, next_y, next_t = \
                BLOCK.xpos, BLOCK.ypos, BLOCK.turn
            if key == pygame.K_UP:
                next_t = (next_t + 1) % 4
            elif key == pygame.K_RIGHT:
                next_x += 1
            elif key == pygame.K_LEFT:
                next_x -= 1
            elif key == pygame.K_DOWN:
                next_y += 1
 
            if not is_overlapped(next_x, next_y, next_t):
                BLOCK.xpos = next_x
                BLOCK.ypos = next_y
                BLOCK.turn = next_t
                BLOCK.data = BLOCK.type[BLOCK.turn]
 
        draw_game_field()
        draw_current_block()
        draw_next_block()
        draw_score(score)
        if game_over:
            draw_gameover_message()
 
        pygame.display.update()
        
runGame()
pygame.quit()
