from random import random, randint

class NN:
    def __init__(self, w=None, b=None):
        self.w = 1 - 2*random() if w is None else w
        self.b = 1 - 2*random() if b is None else b
    
    def think(self, inp):
        output = self.w*inp + self.b
        return 1 if output > 0 else 0

    def mutate(self, mutation_rate=0.01):
        new_nn = NN(w=self.w, b=self.b)

        """if randint(0, 1) == 1: new_nn.w += mutation_rate * new_nn.w
        else: new_nn.w -= mutation_rate * new_nn.w 

        if randint(0, 1) == 1: new_nn.b += mutation_rate * new_nn.b
        else: new_nn.b -= mutation_rate * new_nn.b """
        new_nn.w += mutation_rate * (1 - 2*random())
        new_nn.b += mutation_rate * (1 - 2*random())

        return new_nn