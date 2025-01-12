# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Conversion factor from Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5   # Conversion factor from Celsius to Fahrenheit

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.

    Returns:
    float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # User input for temperature
        temperature = float(input("Enter the temperature to convert: "))  # Use float for more precision
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

        match unit:
            case "f":
                result = convert_to_celsius(temperature)
                print(f"{temperature}°F is {result:}°C")  # Format to 2 decimal places
            case "c":
                result = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {result:}°F")  # Format to 2 decimal places
            case _:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()