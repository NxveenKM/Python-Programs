def main():
    print("Distance Calculator")
    
    # Input coordinates for the first point
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    
    # Input coordinates for the second point
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    
    # Calculate the differences
    delta_x = x2 - x1
    delta_y = y2 - y1
    
    # Calculate the distance using the distance formula
    distance = (delta_x ** 2 + delta_y ** 2) ** 0.5
    
    # Output the result
    print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")

if __name__ == "__main__":
    main()
