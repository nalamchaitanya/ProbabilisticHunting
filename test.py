import Agent
import Environment
import strategy
import copy

environ = Environment.Environment(50)
agent = Agent.Agent(environ)
agent2 = copy.deepcopy(agent)
agent3 = copy.deepcopy(agent)
count3 = agent3.getSearchCount(strategy.maxPair, strategy.manhattan, False)
count = agent.getSearchCount(strategy.maxPair, strategy.manhattan, True)
count2 = agent2.getSearchCount(strategy.maxPairMovingTarget, strategy.manhattan, True)
print(str(count3)+" "+str(count)+" "+str(count2))