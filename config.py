import os
from dotenv import load_dotenv
from agents import Agent,  AsyncOpenAI, OpenAIChatCompletionsModel,Runner
from openai.types.responses import  ResponseTextDeltaEvent
from agents.run import RunConfig
from tools.CheckinSchedulerTool import CheckinSchedule
from tools.GoalAnalyzer import GoalAnalyzer
from tools.MealPlanner import MealPlanner
from tools.Progress_Tracker import ProgressTracker
from tools.WorkoutReccomandation import WorkoutRecommender
from guardrial import health_input_guardrail, health_output_guardrail
from Agent.ecsalation_agent import escalation_agent
from Agent.InjurySupportAgent import injury_support_agent
from Agent.NutritionExpertAgent import nutrition_expert_agent
from agents.exceptions import InputGuardrailTripwireTriggered
from context import UserSessionContext


# Load the environment variables from the .env file
load_dotenv()

gemini_api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)



async def HealthWellness(user_input):
    HealthPlanner = Agent(
        name='Health Wellness Agent',
        instructions="""
Hello! I’m your Health Planner Agent. I'm here to guide you on your wellness journey. If you say hi, I will greet you and assist with your health problems.

1. Ask about goals, fitness level, dietary needs, or any challenges.
2. Analyze input to determine the most appropriate support.
3. Use tools if needed: 
   - Goal Analyzer, Meal Planner, Workout Recommender, etc.
4. Hand off to specialized agents when appropriate:
   - NutritionExpertAgent, InjurySupportAgent, EscalationAgent
""",
        handoffs=[
            escalation_agent,
            injury_support_agent,
            nutrition_expert_agent
        ],
        input_guardrails=[health_input_guardrail],
        output_guardrails=[health_output_guardrail],
        tools=[
            GoalAnalyzer,
            MealPlanner,
            WorkoutRecommender,
            CheckinSchedule,
            ProgressTracker
        ]
    )

    try:
        # Start the run
        response =  Runner.run_streamed(
            starting_agent=HealthPlanner,
            input=user_input,
            context=UserSessionContext
        )

        # Collect streamed response for UI and PDF
        full_response = ""

        async for event in response.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                delta = event.data.delta
                full_response += delta
                print(delta, end="", flush=True)  # For console output

        return full_response  # ✅ Return complete response for UI or PDF

    except InputGuardrailTripwireTriggered as e:
        print("[INPUT ERROR]", e)
        return "❌ Your input is not valid for the health assistant. Please provide more meaningful details (at least 10 characters)."

   
