FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit (✅ simple and correct)
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = int(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

if unit == "C":
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result:.2f}°F")
elif unit == "F":
    result = convert_to_celsius(temperature)
    print(f"{temperature}°F is {result:.2f}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")






