from agents import Agent
from tools import GoalAnalyzer

escalation_agent = Agent(
    name="EscalationAgent",
    instructions="Handle escalations, complaints, or user issues needing special attention.",
    tools=[
        GoalAnalyzer
    ]
)
