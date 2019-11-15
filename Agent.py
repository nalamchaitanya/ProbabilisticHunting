import numpy as np
import random
import copy
import pdb
import Environment
import math

class Agent:
    def __init__(self,env):
        # Initialize the Agent Probability Hunting Matrix using the dimensions of environment
        self.dimension=env.dimension
        self.inCellProb= np.zeros((self.dimension,self.dimension))
        self.foundInCellProb = np.zeros((self.dimension,self.dimension))
        self.falseNeg = [0.1,0.3,0.7,0.9]
        self.env = env
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.foundInCellProb += math.log(1-self.falseNeg[self.env.landscape[i][j]],2)
        self.row = -1
        self.col = -1

    # Updates probability based on the event that row, column doesn't have target
    # P(Bj/Ai) i.e. target not in Bj given Ai (when i=j it is equal to False positive prob of that cell)(Cell Equal)
    # When i not equal to j it is equal to 1(Cells not equal)
    def updateProbability(self, row, column):
        self.inCellProb[row][column] += math.log(self.falseNeg[self.env.landscape[row][column]],2)
        self.foundInCellProb[row][column] += math.log(self.falseNeg[self.env.landscape[row][column]],2)

    # Computes the number of steps taken to reach the target using probabilistic hunting
    def getSearchCount(self, strategy, distance):
        count = 0
        self.row = 0
        self.col = 0
        (row, column) = strategy(self)
        count += distance((0,0), (row,column))
        while(self.env.search(row,column) == False):
            # print("searching : "+str(row)+" "+str(column))
            # pdb.set_trace()
            self.updateProbability(row,column)
            self.row = row
            self.col = column
            (row, column) = strategy(self)
            count += distance((self.row,self.col),(row,column))+1
        return count
