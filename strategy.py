import Agent
import numpy as np
import random
import math

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

# def kCell(row,col,k,agent):
#     ''''This method returns the cell with maximum probability
#     at a distance of k steps from the given position'''
#     matrix=np.zeros((2*k+1,2*k+1))
#     for i in range(-k,k+1,1):
#         for j in range(-k,k+1,1):
#             if 0<=row+i<agent.dimension and 0<=col+j<agent.dimension:
#                 matrix[i+k][j+k]=agent.foundInCellProb[row+i][col+j]
#
#     result=np.where(matrix==np.amax(matrix))
#     list_index=list(zip(result[0],result[1]))
#     i,j=list_index[0]
#     a=row+(i-k)
#     b=col+(j-k)
#     return a,b

def one(a, b):
	return 1

def manhattan(a, b):
	return abs(a[0]-b[0])+abs(a[1]-b[1])

def utility(row,col,agent):
	k = 5
	matrix = np.zeros((2 * k + 1, 2 * k + 1))
	# dist=0
	for i in range(-k, k + 1, 1):
		for j in range(-k, k + 1, 1):
			if i == 0 and j == 0:
				matrix[k][k] = -math.inf
			elif 0 <= row + i < agent.dimension and 0 <= col + j < agent.dimension:
				dist = abs(i) + abs(j)
				matrix[i + k][j + k] = (agent.inCellProb[row + i][col + j])/dist
			else:
				matrix[i + k][j + k] = -math.inf
	util_List = []
	for c in range(10):
		result = np.where(matrix == np.amax(matrix))
		list_index = list(zip(result[0], result[1]))
		if len(list_index) == 0:
			print(np.amax(matrix))
			print(matrix)
		(a, b) = list_index[0]
		if matrix[a][b] == -math.inf:
			break
		matrix[a][b] = -math.inf
		a = row + (a - k)
		b = col + (b - k)
		util_List.append((a, b))
	return util_List

def pairUtility(a, b, s, agent):
	da = abs(s[0]-a[0])+abs(s[1]-a[1])
	ab = abs(a[0]-b[0])+abs(a[1]-b[1])
	cost = (-agent.inCellProb[a[0]][a[1]])*da + 1 + (-agent.inCellProb[b[0]][b[1]])*ab + 1
	return cost

def maxPair(agent):
	row = agent.row
	col = agent.col
	minCost = math.inf
	minx = 0
	miny = 0
	utilList = utility(row, col, agent)
	for i in range(len(utilList)):
		for j in range(len(utilList)):
			if i != j:
				cost = pairUtility(utilList[i], utilList[j], (row, col), agent)
				if cost < minCost:
					minCost = cost
					minx = utilList[i][0]
					miny = utilList[i][1]
	return (minx, miny)