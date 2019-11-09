import numpy as np
import random
import copy

#random.seed(1)
class Environment:
    def __init__(self, d):
        '''
        d -> int : Dimension of board
        flat->0, P(flat)=0.2
        hilly->1, P(hilly)=0.3
        forest->2, P(forest)=0.3 
        caves->3, P(caves)=0.2
        target->(int,int) : Coordinates of the target. 
        '''
        self.dimension = d
        self.landscape = np.zeros((self.dimension,self.dimension))
        for i in range(self.dimension):
            for j in range(self.dimension):
                prob = random.uniform(0,1)
                if prob<0.2:
                    self.landscape[i][j] = 0
                elif prob<0.5:
                    self.landscape[i][j] = 1
                elif prob<0.8:
                    self.landscape[i][j] = 2
                else:
                    self.landscape[i][j] = 3    

       self.target = (random.uniform(0,self.dimension-1), random.uniform(0,self.dimension-1))


    def search(self, row, column):
        '''
        Given a row and column search according to it's landscape and return success or failure.
        '''

        #P(target not found | target in cell):
        d = {0:0.1, 1:0.3, 2:0.7, 3:0.9}
        if (row,column) != self.target:
            return False
        else:
            if random.uniform(0,1) < d[self.landscape[row][column]]:
                return False
            else:
                return True


        