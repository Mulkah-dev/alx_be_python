import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))  # 🔴 CHANGED: added formatting
    return current_date  # 🔴 ADDED: return the date for later use

# 🔴 ADDED: Save the returned date so we can use it to calculate the future date
current_date = display_current_datetime()

# Ask the user how many days to add
days = int(input("Enter number of days: "))

def calculate_future_date(start_date, days_to_add):  # 🔴 CHANGED: accepts date and number of days
    future_date = start_date + datetime.timedelta(days=days_to_add)  # 🔴 CHANGED: uses timedelta
    print("Future date:", future_date.strftime("%Y-%m-%d"))  # 🔴 CHANGED: print in proper format

# 🔴 ADDED: Call the function with current date and days
calculate_future_date(current_date, days)
