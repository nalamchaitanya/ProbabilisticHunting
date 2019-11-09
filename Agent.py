"""
"""
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
        self.probLandscape= np.zeros((self.dimension,self.dimension))
        self.falseNeg = [0.1,0.3,0.7,0.9]
        self.env = env

    def chooseNextCell(self):
        # This function returns coordinates of cell having Max Probability
        result = np.where(self.probLandscape == np.amax(self.probLandscape))
        list_index=list(zip(result[0],result[1]))
        return list_index[0]

    # Updates probability based on the event that row, column doesn't have target
    def updateProbability(self, row, column):
        self.probLandscape[row][column] += math.log(self.falseNeg[self.env.landscape[row][column]],2)

    # Computes the number of steps taken to reach the target using probabilistic hunting
    def getSearchCount(self):
        count = 0
        (row, column) = self.chooseNextCell()
        while(self.env.search(row,column) == False):
            print("searching : "+str(row)+" "+str(column))
            count += 1
            # pdb.set_trace()
            self.updateProbability(row,column)
            (row, column) = self.chooseNextCell()
        return count
