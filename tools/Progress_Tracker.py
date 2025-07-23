from agents import function_tool

@function_tool
def ProgressTracker(user_input: str) -> str:
    """
    Tracks user progress based on latest updates.
    Example input: "I lost 2 kg and worked out 3 times this week."
    """
    return (
        "📈 Progress Tracker Tool Launched!\n"
        "Here's your weekly progress summary:\n\n"
        "**Weight Change:** -2 kg\n"
        "**Workout Adherence:** Great job completing 3 sessions!\n"
        "**Mood & Energy:** Looking stable\n\n"
        "Keep up the great work. You're on the right path!"
    )
