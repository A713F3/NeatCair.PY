import pygame
import board

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

WIDTH = COL * SIZE
HEIGHT = ROW * SIZE

"""BOARDS = []
for r in range(ROW):
    row = []
    for c in range(COL):
        row.append(Board(c%2, r%2))

    BOARDS.append(row)
"""

screen = pygame.display.set_mode([WIDTH, HEIGHT])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for r in range(ROW):
        for c in range(COL):
            #board = BOARDS[r][c]

            pygame.draw.rect(screen, (255, 255, 255), (c*SIZE, r*SIZE, c*SIZE + SIZE, r*SIZE + SIZE), 10)

    pygame.display.update()



pygame.quit()