import Agent
import Environment
import strategy
import copy

environ = Environment.Environment(50)
agent = Agent.Agent(environ)
count = agent.getSearchCount(strategy.maxPair, strategy.manhattan, True)
agent2 = copy.deepcopy(agent)
count2 = agent.getSearchCount(strategy.maxPairMovingTarget, strategy.manhattan, True)
print(str(count)+" "+str(count2))