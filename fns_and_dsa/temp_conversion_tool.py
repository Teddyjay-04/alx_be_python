# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function to handle user input and perform temperature conversions.
    """
    try:
        # Validate temperature input
        temperature_input = input("Enter the temperature to convert: ").strip()
        if not temperature_input.replace('.', '', 1).isdigit() or temperature_input.count('.') > 1:
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(temperature_input)

        # Validate unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()
        match unit:
            case "f":
                result = convert_to_celsius(temperature)
                print(f"{temperature}F is {result:.2f}C")
            case "c":
                result = convert_to_fahrenheit(temperature)
                print(f"{temperature}C is {result:.2f}F")
            case _:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()