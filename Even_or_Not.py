try:
    # Get user input
    num = int(input("Enter a number: "))
    
    # Check if the number is even
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
except ValueError:
    print("Please enter a valid integer.")
