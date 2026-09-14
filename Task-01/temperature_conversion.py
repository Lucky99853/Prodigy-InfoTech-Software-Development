# Task-01: Temperature Conversion Program

print("Temperature Conversion Program")
print("-------------------------------")

# Get temperature from user
temperature = float(input("Enter temperature: "))

# Get original unit
unit = input(
    "Enter the original unit (Celsius, Fahrenheit, or Kelvin): "
).strip().lower()

# Celsius conversion
if unit == "celsius":
    fahrenheit = (temperature * 9 / 5) + 32
    kelvin = temperature + 273.15

    print("\nConverted Temperature:")
    print("Fahrenheit:", round(fahrenheit, 2), "°F")
    print("Kelvin:", round(kelvin, 2), "K")

# Fahrenheit conversion
elif unit == "fahrenheit":
    celsius = (temperature - 32) * 5 / 9
    kelvin = (temperature - 32) * 5 / 9 + 273.15

    print("\nConverted Temperature:")
    print("Celsius:", round(celsius, 2), "°C")
    print("Kelvin:", round(kelvin, 2), "K")

# Kelvin conversion
elif unit == "kelvin":
    celsius = temperature - 273.15
    fahrenheit = (temperature - 273.15) * 9 / 5 + 32

    print("\nConverted Temperature:")
    print("Celsius:", round(celsius, 2), "°C")
    print("Fahrenheit:", round(fahrenheit, 2), "°F")

# Invalid unit
else:
    print("\nInvalid unit!")
    print("Please enter Celsius, Fahrenheit, or Kelvin.")
