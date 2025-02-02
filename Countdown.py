# Main program
while True:
    try:
        # Get user input
        number = int(input("Enter a number to start the countdown: "))
        break  # Exit the loop if input is valid
    except ValueError:
        print("Please enter a valid integer.")

# Countdown using a while loop
print("Countdown starting...")
while number >= 0:
    print(number)
    number -= 1  # Decrease the number by 1

print("Countdown complete!")
