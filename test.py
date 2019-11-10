import Agent
import Environment

environ = Environment.Environment(50)
agent = Agent.Agent(environ)
print (agent.getSearchCount())
