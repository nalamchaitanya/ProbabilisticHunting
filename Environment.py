import numpy as np
import random
import copy

#random.seed(1)
class Environment:
    def __init__(self, d):
        '''
        d -> int : Dimension of board
        flat -> 1
        hilly -> 2
        forest -> 3
        caves -> 4
        '''
        self.dimension = d



    def search(self, row, column):
        '''
        Given a row and column search according to it's landscape and return success or failure.
        '''
        