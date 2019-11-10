import Agent
import Environment
import strategy
import random
import copy

environ = Environment.Environment(50)
isInCellcount = 0
isFoundInCellcount = 0
iterations = 1000
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

print ("Average count for isInCell : "+str(isInCellcount/100))
print ("Average count for isFoundInCell : "+str(isFoundInCellcount/100))