# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Ensure the size is positive
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize the row counter
    row = 0
    
    # Use a while loop to iterate through each row
    while row < size:
        # Use a for loop to print asterisks side by side
        for col in range(size):
            print("*", end="")
        # Print a newline character to move to the next row
        print()
        # Increment the row counter
        row += 1