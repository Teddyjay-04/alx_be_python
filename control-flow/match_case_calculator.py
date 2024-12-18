first_number = input("Enter the first number:")
second_number = input("Enter the second number")

operation = input("Choose the operation (+, -, *, /):")

if operation == "+":
    result = float(first_number) + float(second_number)
    print("The result is:", result)

elif operation == "-":
    result = float(first_number) - float(second_number)
    print("The result is:", result)

elif operation == "*":
    result = float(first_number) * float(second_number)
    print("The result is:", result)

elif operation == "/":
    if second_number != "0":
        result = float(first_number) / float(second_number)
        print("The result is:", result)
    else:
        print("Cannot be divided by zero")
