"""
"""
import numpy as np
import random
import copy
import pdb
import numpy as np
# 
class Agent:
    def __init__(self,env):
        # Initialize the Agent Probability Hunting Matrix using the dimensions of environment
        self.dimension=env.dimension
        self.probLandscape= np.zeros((self.dimension,self.dimension))


    def chooseNextCell(self):
        # This function returns coordinates of cell having Max Probability
        result = np.where(self.probLandscape == np.amax(self.probLandscape))
        list_index=list(zip(result[0],result[1]))
        return list_index[0]

    def updateProbability(self, row, column):