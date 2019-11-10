import Agent
import numpy as np
import random

def isInCell(agent):
        # This function returns coordinates of cell having Max Probability
        # amax returns max number in the matrix
        # list_index has all the coordinates with max number
        result = np.where(agent.inCellProb == np.amax(agent.inCellProb))
        list_index=list(zip(result[0],result[1]))
        return list_index[int(random.uniform(0,len(list_index)))]
        # return list_index[0]

def isFoundInCell(agent):
    result = np.where(agent.foundInCellProb == np.amax(agent.foundInCellProb))
    list_index=list(zip(result[0],result[1]))
    return list_index[int(random.uniform(0,len(list_index)))]
    # return list_index[0]