import Agent
import Environment
import strategy
import random
import copy
import matplotlib.pyplot as plt
import pandas as pd
import statistics
from collections import Counter

iterations = 50
median1List = []
median2List = []
mean1List = []
mean2List = []
mode1List = []
mode2List = []
for d in range(20,110,10):
	environ = Environment.Environment(d)
	isInCellcount = []
	isFoundInCellcount = []
	for i in range(iterations):
		environ.count = 0
		environ.target = (int(random.uniform(0,environ.dimension-1)), int(random.uniform(0,environ.dimension-1)))
		agent = Agent.Agent(environ)
		# agent2 = copy.deepcopy(agent)
		agent3 = copy.deepcopy(agent)
		count1 = agent.getSearchCount(strategy.isInCell, strategy.manhattan)
		# count2 = agent2.getSearchCount(strategy.isFoundInCell, strategy.one)
		count2 = agent3.getSearchCount(strategy.maxPair, strategy.manhattan)
		print(str(count1)+" "+str(count2))
		isInCellcount.append(count1)
		isFoundInCellcount.append(count2)
	# Do median and mode and etc caclculation here.
	print("d : "+str(d))
	isInCellcount.sort()
	median1 = statistics.median(isInCellcount)#[len(isInCellcount)/2]
	mean1 = float(sum(isInCellcount[iterations//4:3*iterations//4]))/(iterations/2)
	isFoundInCellcount.sort()
	median2 = statistics.median(isFoundInCellcount)#[len(isFoundInCellcount)/2]
	mean2 = float(sum(isFoundInCellcount[iterations//4:3*iterations//4]))/(iterations/2)
	mean1List.append(float(mean1)/(d*d))
	mean2List.append(float(mean2)/(d*d))
	median1List.append(float(median1)/(d*d))
	median2List.append(float(median2)/(d*d))

	# isInCellcount1 = [float(x)/(d*d) for x in isInCellcount]
	# isInCellcountBin = pd.cut(isInCellcount1, [0,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9])
	# isFoundInCellcount1 = [float(x)/(d*d) for x in isFoundInCellcount]
	# isFoundInCellcountBin = pd.cut(isFoundInCellcount1, [0,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9])
	# counter1 = Counter(isInCellcountBin)
	# counter2 = Counter(isFoundInCellcountBin)
	# mode_count1 = max(counter1.values())
	# mode_count2 = max(counter2.values())
	# mode1 = [key for key, count in counter1.items() if count == mode_count1]
	# mode2 = [key for key, count in counter2.items() if count == mode_count2]
	# mode1List.append(mode1[0])
	# mode2List.append(mode2[0])


print('mean1: '+str(mean1List))
print('mean2: '+str(mean2List))
print('median1: '+str(median1List))
print('median2: '+str(median2List))
# print('mode1: '+str(mode1List))
# print('mode2: '+str(mode2List))




fig = plt.figure()
dimensionList = range(20,110,10)
plt.plot(dimensionList, median1List,label="Rule 1")
plt.plot(dimensionList, median2List, label="Rule 2")
plt.xlabel('Dimension')
plt.ylabel('Median of action count / No of cells')
plt.title('Rule 1 vs Utility')
plt.legend()
plt.show()

fig2 = plt.figure()
# dimensionList = range(20,80,10)
plt.plot(dimensionList, mean1List,label="Rule 1")
plt.plot(dimensionList, mean2List, label="Utility")
plt.xlabel('Dimension')
plt.ylabel('Mean of action count / No of cells')
plt.title('Rule 1 vs Utility')
plt.legend()
plt.show()

# print ("Average count for isInCell : "+str(inCellCountList))
# print ("Average count for isFoundInCell : "+str(foundInCellCountList))
