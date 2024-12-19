# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". You can complete it when you have time."
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that should be addressed soon."
        else:
            reminder += ". Consider completing it when you can."
    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " but it's not urgent."
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

# Provide the customized reminder
print(f"Reminder: {reminder}")

'''# Additional message for completion
if priority in ["high", "medium", "low"]:
    print("Well done on completing this project! Let the world hear about this milestone achieved.")
    print("🚀 Click here to tweet! 🚀")'''