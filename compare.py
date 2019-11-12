import Agent
import Environment
import strategy
import random
import copy

iterations = 100
inCellCountList = []
foundInCellCountList = []
for d in range(40,70,10):
	environ = Environment.Environment(d)
	isInCellcount = 0
	isFoundInCellcount = 0
	for i in range(iterations):
		environ.count = 0
		environ.target = (int(random.uniform(0,environ.dimension-1)), int(random.uniform(0,environ.dimension-1)))
		agent = Agent.Agent(environ)
		agent2 = copy.deepcopy(agent)
		count1 = agent.getSearchCount(strategy.isInCell)
		count2 = agent2.getSearchCount(strategy.isFoundInCell)
		print(str(count1)+" "+str(count2))
		isInCellcount += count1
		isFoundInCellcount += count2
	inCellCountList.append(float(isInCellcount)/(iterations*d*d));
	foundInCellCountList.append(float(isFoundInCellcount)/iterations*d*d);

print ("Average count for isInCell : "+str(inCellCountList))
print ("Average count for isFoundInCell : "+str(foundInCellCountList))