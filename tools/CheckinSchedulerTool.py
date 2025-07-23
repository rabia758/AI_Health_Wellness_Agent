from agents import function_tool
from datetime import datetime, timedelta


@function_tool
def CheckinSchedule(user_input: str) -> str:
    """
    Schedule a check-in for the user based on their request.
    Example input: "I want to schedule my next check-in."
    """
    # Example logic: next check-in in 7 days from today
    next_checkin_date = datetime.now() + timedelta(days=7)
    formatted_date = next_checkin_date.strftime("%A, %d %B %Y at %I:%M %p")

    return (
        f"🗓 Check-in Scheduled!\n"
        f"Your next check-in has been set for **{formatted_date}**.\n"
        "Make sure to stay on track and submit your updates!"
    )