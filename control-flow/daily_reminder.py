task = input("Enter your task:")
priority = input("Enter the task's priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

if time_bound == "yes":
    match priority:
        case "high":
            print("Reminder:", task, "is a", priority, "priority task that requires immediate action today!")
        case "medium":
            print("Reminder:", task, "is a", priority, "priority task that requires action today!")
        case "low":
            print("Reminder:", task, "is a", priority, "priority task. Consider completing it when you have free time")
else:
    match priority:
        case "high":
            print("Reminder:", task, "is a", priority, "priority task. Plan to do it soon even though it's not urgent.")
        case "medium":
            print("Reminder:", task, "is a", priority, "priority task. Add it to your schedule for this week.")
        case "low":
            print("Reminder:", task, "is a", priority, "priority task. Do it when you have spare time.")        


