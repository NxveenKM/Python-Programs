# Main program
try:
    # Get user input
    number = int(input("Enter a number to start the countdown: "))
    
    # Countdown from the number to zero
    for i in range(number, -1, -1):  # Start from 'number' down to 0
        print(i)
except ValueError:
    print("Please enter a valid integer.")
