import Agent
import numpy as np
import random

def isInCell(agent):
    ''''
    This function returns coordinates of cell having Max Probability
    amax returns max number in the matrix
    list_index has all the coordinates with max number
    '''
    result = np.where(agent.inCellProb == np.amax(agent.inCellProb))
    list_index=list(zip(result[0],result[1]))
    return list_index[int(random.uniform(0,len(list_index)))]
    # return list_index[0]

def isFoundInCell(agent):
    result = np.where(agent.foundInCellProb == np.amax(agent.foundInCellProb))
    list_index=list(zip(result[0],result[1]))
    return list_index[int(random.uniform(0,len(list_index)))]
    # return list_index[0]

def kCell(row,col,k,agent):
    ''''This method returns the cell with maximum probability
    at a distance of k steps from the given position'''
    matrix=np.zeros((2*k+1,2*k+1))
    for i in range(-k,k+1,1):
        for j in range(-k,k+1,1):
            if 0<=row+i<agent.dimension and 0<=col+j<agent.dimension:
                matrix[i+k][j+k]=agent.foundInCellProb[row+i][col+j]

    result=np.where(matrix==np.amax(matrix))
    list_index=list(zip(result[0],result[1]))
    i,j=list_index[0]
    a=row+(i-k)
    b=col+(j-k)
    return a,b