Task = input("Enter your Task:")
Priority = input("Enter the Task's Priority (high,medium,low):")
Time_bound = input("Is it time-bound? (yes/no):")

if Time_bound == "yes":
    match Priority:
        case "high":
            print("Reminder:", Task, "is a", Priority, "Priority Task that requires immediate action today!")
        case "medium":
            print("Reminder:", Task, "is a", Priority, "Priority Task that requires action today!")
        case "low":
            print("Reminder:", Task, "is a", Priority, "Priority Task. Consider completing it when you have free time")
else:
    match Priority:
        case "high":
            print("Reminder:", Task, "is a", Priority, "Priority Task. Plan to do it soon even though it's not urgent.")
        case "medium":
            print("Reminder:", Task, "is a", Priority, "Priority Task. Add it to your schedule for this week.")
        case "low":
            print("Reminder:", Task, "is a", Priority, "Priority Task. Do it when you have spare time.")        


