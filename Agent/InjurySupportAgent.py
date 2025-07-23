from agents import Agent
from tools import Progress_Tracker

injury_support_agent = Agent(
    name="InjurySupportAgent",
    instructions="Assist users with injury-related concerns and recommend care or modifications.",
    tools=[
        Progress_Tracker
    ]
   
)