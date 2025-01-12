# Conversion factors
FAHRENHEIT_TO_CELSIUS = 5/9
CELSIUS_TO_FAHRENHEIT = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT) + 32

def main():
    while True:
        try:
            temperature = float(input("Enter temperature: "))
            break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

    unit = input("Is it Celsius or Fahrenheit? (C/F): ").upper()

    while unit not in ["C", "F"]:
        unit = input("Invalid unit. Please enter C for Celsius or F for Fahrenheit: ").upper()

    if unit == "C":
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
    elif unit == "F":
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")

if __name__ == "__main__":
    main()
