# File to read from
filename = "example.txt"  # Replace with your actual file name

try:
    with open(filename, 'r') as file:
        print("Reversed lines:\n")
        for line in file:
            reversed_line = line.rstrip('\n')[::-1]  # Remove newline, then reverse
            print(reversed_line)
except FileNotFoundError:
    print(f"File '{filename}' not found.")
