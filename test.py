import Agent
import Environment
import strategy
import copy

environ = Environment.Environment(50)
agent = Agent.Agent(environ)
agent2 = copy.deepcopy(agent)
print (agent.getSearchCount(strategy.isInCell))
print (agent2.getSearchCount(strategy.isFoundInCell))
