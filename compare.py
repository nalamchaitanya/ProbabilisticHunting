import Agent
import Environment
import strategy
import random
import copy
import matplotlib.pyplot as plt

iterations = 100
median1List = []
median2List = []
mean1List = []
mean2List = []
for d in range(20,80,10):
	environ = Environment.Environment(d)
	isInCellcount = []
	isFoundInCellcount = []
	for i in range(iterations):
		environ.count = 0
		environ.target = (int(random.uniform(0,environ.dimension-1)), int(random.uniform(0,environ.dimension-1)))
		agent = Agent.Agent(environ)
		agent2 = copy.deepcopy(agent)
		count1 = agent.getSearchCount(strategy.isInCell)
		count2 = agent2.getSearchCount(strategy.isFoundInCell)
		print(str(count1)+" "+str(count2))
		isInCellcount.append(count1)
		isFoundInCellcount.append(count2)
	# Do median and mode and etc caclculation here.
	isInCellcount.sort()
	median1 = isInCellcount[len(isInCellcount)/2]
	mean1 = float(sum(isInCellcount[iterations/4:3*iterations/4]))/(iterations/2)
	isFoundInCellcount.sort()
	median2 = isFoundInCellcount[len(isFoundInCellcount)/2]
	mean2 = float(sum(isFoundInCellcount[iterations/4:3*iterations/4]))/(iterations/2)
	mean1List.append(float(mean1)/(d*d))
	mean2List.append(float(mean2)/(d*d))
	median1List.append(float(median1)/(d*d))
	median2List.append(float(median2)/(d*d))

fig = plt.figure()
dimensionList = range(20,80,10)
plt.plot(dimensionList, inCellCountList,label="Rule 1")
plt.plot(dimensionList, foundInCellCountList, label="Rule 2")
plt.xlabel('Dimension')
plt.ylabel('Median of search count / No of cells')
plt.title('Rule 1 vs 2')
plt.show()

fig2 = plt.figure()
# dimensionList = range(20,80,10)
plt.plot(dimensionList, mean1List,label="Rule 1")
plt.plot(dimensionList, mean2List, label="Rule 2")
plt.xlabel('Dimension')
plt.ylabel('Median of search count / No of cells')
plt.title('Rule 1 vs 2')
plt.show()

# print ("Average count for isInCell : "+str(inCellCountList))
# print ("Average count for isFoundInCell : "+str(foundInCellCountList))