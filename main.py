import pygame
from board import *
from random import randint
from time import time


class Object:
    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        self.color = color

    def draw(self, screen, x, y):
        pygame.draw.rect(screen, self.color, (x, y, self.w, self.h))

pygame.init()
font = pygame.font.Font(None, 30)

ROW = 4
COL = 4

SIZE = 150
PD = 5
DSIZE = SIZE - 2*PD

WIDTH = COL * SIZE
HEIGHT = ROW * SIZE

CAR = Object(30, DSIZE//4, (255, 0, 0))
LOG = Object(15, DSIZE//4, (139, 69, 19))
LANE = Object(10, DSIZE, (100, 100, 100))
ROAD = Object(DSIZE, DSIZE, (20, 20, 20))

BOARDS = []
for r in range(ROW):
    row = []
    for c in range(COL):
        board = Board(randint(0, 1), randint(0, 1))
        row.append(board)

    BOARDS.append(row)


screen = pygame.display.set_mode([WIDTH, HEIGHT])

gens = 0
best_score = 0
prev_best_score = 0

prev_time = time()

running = True
while running:
    cur_time = time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for r in range(ROW):
        for c in range(COL):
            board = BOARDS[r][c]

            x = c*SIZE + PD
            y = r*SIZE + PD
            
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
            
            log_y = y + board.log_pos

            LOG.draw(screen, log_x, log_y)

            #Move Logs
            if board.is_active:
                board.update(car=DSIZE - CAR.h - LOG.h, limit=DSIZE - LOG.h)
            
            screen.blit(font.render(str(board.score), True, CAR.color), (x, y))

    best_board = bestBoard(BOARDS)
    if best_board.score > best_score: best_score = best_board.score

    if allBoardsNotActive(BOARDS) or cur_time - prev_time > 10:
        gens += 1
        prev_best_score = best_board.score

        prev_time = time()
        resetBoards(BOARDS, best_board, 0.1)

    info_text = f"Gens:{gens} Best Score:{best_score} Prev Best Score:{prev_best_score}"
    screen.blit(font.render(info_text, True, (150, 150, 150)), (10, HEIGHT-30))
            
        
    pygame.display.update()

pygame.quit()