from agents import function_tool

@function_tool
def MealPlanner(user_input: str) -> str:
    """
    Generates a personalized meal plan.
    Example input: "I prefer a vegetarian diet under 1800 calories."
    """
    return (
        "🍽 Meal Planner Tool Executed!\n"
        "A customized vegetarian meal plan has been generated for an 1800 kcal target.\n\n"
        "**Breakfast:** Oatmeal with almond milk and berries\n"
        "**Lunch:** Quinoa salad with chickpeas and avocado\n"
        "**Dinner:** Grilled tofu with stir-fried vegetables\n\n"
        "Stay consistent and track your meals to ensure steady progress!"
    )
