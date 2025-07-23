from agents import Agent
from tools import MealPlanner


nutrition_expert_agent = Agent(
    name="NutritionExpertAgent",
    instructions="Provide expert-level nutrition guidance and meal planning.",
    tools=[
        MealPlanner,
    ]
)