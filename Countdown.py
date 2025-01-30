# Main program
try:
    # Get user input
    number = int(input("Enter a number to start the countdown: "))
    
    # Countdown using a while loop
    while number >= 0:
        print(number)
        number -= 1  # Decrease the number by 1
except ValueError:
    print("Please enter a valid integer.")
