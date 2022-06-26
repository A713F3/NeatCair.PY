from random import random

class NN:
    def __init__(self):
        self.w = random()
        self.b = random()
    
    def think(self, inp):
        output = self.w*inp + self.b
        return 1 if output > 0.5 else 0

    def mutate(self, mutation_rate=0.01):
        new_nn = NN()
        new_nn.w = self.w * mutation_rate
        new_nn.b = self.b * mutation_rate

        return new_nn