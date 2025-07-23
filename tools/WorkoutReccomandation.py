from agents import function_tool

@function_tool
def WorkoutRecommender(user_input: str) -> str:
    """
    Recommends a workout routine.
    Example input: "I want to work out 4 times a week to lose fat."
    """
    return (
        "💪 Workout Recommender Tool Completed!\n"
        "Here's your custom 4-day weekly fat-burning workout plan:\n\n"
        "**Monday:** 30 mins HIIT\n"
        "**Wednesday:** Bodyweight Strength Circuit\n"
        "**Friday:** Cardio & Core\n"
        "**Saturday:** Yoga or Active Recovery\n\n"
        "Stay active and aligned with your goals!"
    )
