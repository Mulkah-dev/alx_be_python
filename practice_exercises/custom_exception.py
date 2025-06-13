# Step 1: Create a custom exception class
class ValueTooHighError(Exception):
    pass

try:
    # Step 2: Get user input and convert to integer
    number = int(input("Enter a number: "))

    # Step 3: Check condition and raise exception if needed
    if number > 100:
        raise ValueTooHighError(f"{number} is greater than 100")

    print("You entered:", number)

# Step 4: Handle the custom exception
except ValueTooHighError as e:
    print("Error:", e)


