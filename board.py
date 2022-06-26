class Board:
    def __init__(self, car_lane=0, log_lane=0, log_pos=0):
        self.car_lane = car_lane
        self.log_lane = log_lane

        self.log_pos = log_pos

    def move_log(self, velo=1, car=100, limit=150):
        self.log_pos += velo
        
        if self.log_pos >= car and self.log_lane == self.car_lane:
            self.log_pos = 0
        
        if self.log_pos >= limit:
            self.log_pos = 0

class Object:
    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        self.color = color
    