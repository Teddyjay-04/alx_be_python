task = str(input("Enter your task:"))

priority = int(input("Priority (high/medium/low):"))

time_bound = int(input("Is it time-bound? (yes/no):"))

if time_bound == 'yes':
    print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
elif time_bound == 'no':
    print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")