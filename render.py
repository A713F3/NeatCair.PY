import pygame
from board import Board, Object


class Object:
    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        self.color = color

    def draw(self, screen, x, y):
        pygame.draw.rect(screen, self.color, (x, y, self.w, self.h)) 

pygame.init()

"""
20 border
__________________
5 padding

65 car  65 log

5 padding
___________________

10 lane ===========
___________________
5 padding

5 padding
___________________
20 border
"""

ROW = 3
COL = 3

SIZE = 200
PD = 5
DSIZE = SIZE - 2*PD

WIDTH = COL * SIZE
HEIGHT = ROW * SIZE

CAR = Object(30, DSIZE//4, (255, 0, 0))
LOG = Object(15, DSIZE//4, (139, 69, 19))
LANE = Object(10, DSIZE, (200, 200, 200))
ROAD = Object(DSIZE, DSIZE, (20, 20, 20))

BOARDS = []
for r in range(ROW):
    row = []
    for c in range(COL):
        board = Board(0, 0)
        row.append(board)

    BOARDS.append(row)


screen = pygame.display.set_mode([WIDTH, HEIGHT])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for r in range(ROW):
        for c in range(COL):
            board = BOARDS[r][c]

            x = c*SIZE+PD
            y = r*SIZE+PD
            
            #Background
            ROAD.draw(screen, x, y)

            #Lane
            lane_x = x + DSIZE//2 - LANE.w//2
            LANE.draw(screen, lane_x, y)

            #Car
            if board.car_lane == 0:
                car_x = x + DSIZE//4 - CAR.w//2
            if board.car_lane == 1:
                car_x = x + 3*DSIZE//4 - CAR.w//2
            
            car_y = y + 3*CAR.h

            CAR.draw(screen, car_x, car_y)

            #Log
            if board.log_lane == 0:
                log_x = x + DSIZE//4 - LOG.w//2
            if board.log_lane == 1:
                log_x = x + 3*DSIZE//4 - LOG.w//2
            
            log_y = y+board.log_pos

            LOG.draw(screen, log_x, log_y)

            #Move Logs
            board.move_log(car=DSIZE - CAR.h - LOG.h, limit=DSIZE - LOG.h)
            

    pygame.display.update()



pygame.quit()