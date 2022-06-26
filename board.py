from random import randint
from nn import NN

class Board:
    def __init__(self, car_lane=0, log_lane=0, log_pos=0):
        self.is_active = True

        self.score = 0

        self.nn = NN()

        self.car_lane = car_lane
        self.log_lane = log_lane

        self.log_pos = log_pos

    def update(self, velo=1, car=100, limit=150):
        self.log_pos += velo
        
        if self.log_pos >= car and self.log_lane == self.car_lane:
            self.is_active = False
        
        if self.log_pos >= limit:
            self.log_pos = 0
            self.log_lane = randint(0, 1)
            self.score += 1

            self.car_lane = self.nn.think(self.log_lane)

    def reset(self):
        self.car_lane = randint(0, 1)
        self.log_lane = randint(0, 1)
        self.log_pos = 0
        self.is_active = True
        self.score = 0

def allBoardsNotActive(boards):
    for r in range(len(boards)):
        for c in range(len(boards[r])):
            if boards[r][c].is_active:
                return False
    return True

def bestBoard(boards):
    best_board = boards[0][0]

    for r in range(len(boards)):
        for c in range(len(boards[r])):
            if not boards[r][c].score >= best_board.score:
                best_board = boards[r][c]

    return best_board 