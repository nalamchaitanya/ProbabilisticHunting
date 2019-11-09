import Agent
import Environment

environ = Environment.Environment(10)
agent = Agent.Agent(environ)
print agent.getSearchCount()
