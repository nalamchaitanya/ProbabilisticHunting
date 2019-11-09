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

    def chooseNextCell(self):
        # This function returns coordinates of cell having Max Probability
        result = np.where(self.probLandscape == np.amax(self.probLandscape))
        list_index=list(zip(result[0],result[1]))
        return list_index[0]

    def updateProbability(self, row, column):
        self.probLandscape[row][column] += math.log(falseNeg[env.landscape(row,column)],2)

    def getSearchCount(self):
        count = 0
        (row, column) = self.chooseNextCell()
        while(!self.env.search(row,column)):
            count += 1
            self.updateProbability(row,column)
            (row, column) = self.chooseNextCell()
        return count
