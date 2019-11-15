import numpy as np
import random
import copy

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
        self.count = 0
        self.landscape = np.ndarray(shape=(self.dimension,self.dimension), dtype=int)
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
        self.target = (int(random.uniform(0,self.dimension-1)), int(random.uniform(0,self.dimension-1)))

    def search(self, row, column):
        '''
        Given a row and column search according to it's landscape and return success or failure.
        '''
        #P(target not found | target in cell):
        d = {0:0.1, 1:0.3, 2:0.7, 3:0.9}

        if (row,column) != self.target:
            self.count+=1
            return False
        else:
            if random.uniform(0,1) < d[self.landscape[row][column]]:
                self.count += 1
                # print("Target found but not found" + " " + str(self.count)+" " + str(self.landscape[row][column]))
                return False
            else:
                return True

    def move_Target(self):
        row_Target , col_Target = self.target
        list_neighbours=[]
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i == 0 and j == 0:
                    continue
                elif i*j == 0 and (0<=row_Target+i<self.dimension and 0<=col_Target+j<self.dimension):
                    list_neighbours.append((row_Target+i,col_Target+j))

        self.target= list_neighbours[int(random.uniform(0,len(list_neighbours)))]

    def getTargetTerrainType(self):
        actual_Terrain=self.landscape[self.target[0]][self.target[1]]
        if actual_Terrain==0:
            return random.choice([1,2,3])
        elif actual_Terrain==1:
            return random.choice([0, 2, 3])
        elif actual_Terrain==2:
            return random.choice([0, 1, 3])
        elif actual_Terrain==3:
            return random.choice([0, 1, 2])
