
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def get_temperature():
while True:
try:
temperature = float(input("Enter temperature: "))
return temperature
except ValueError:
print("Invalid temperature. Please enter a numeric value.")

def get_unit():
while True:
unit = input("Is it Celsius or Fahrenheit? (C/F): ").upper()
if unit in ["C", "F"]:
return unit
else:
print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")

def main():
print("Temperature Conversion Tool")
print("--------------------------------")

temperature = get_temperature()
unit = get_unit()

if unit == "C":
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
elif unit == "F":
    print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")

while True:
    again = input("Do you want to convert another temperature? (Y/N): ").upper()
    if again == "Y":
        main()
    elif again == "N":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please enter Y for Yes or N for No.")

if name == "main":
main()

