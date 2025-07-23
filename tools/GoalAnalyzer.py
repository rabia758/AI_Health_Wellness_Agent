from agents import function_tool

@function_tool
def GoalAnalyzer(user_input: str) -> str:
    
    """
    Analyzes user goals from the input.
    Example input: "I want to lose 5 kg in 2 months and build stamina."
    """
    return (
        
        "🎯 Goal Analyzer Tool Activated!\n"
        "We've analyzed your input and identified your key health goals.\n\n"
        "**Goal Type:** Likely Weight Loss and Stamina Building\n"
        "**Duration:** Estimated 2 months\n"
        "**Focus Areas:** Balanced Diet, Cardio Training, Hydration\n\n"
        "Let’s now generate your meal and workout plans to support these goals!"
    )
