from collections import defaultdict

# File to read from (C program or text file)
filename = "example.c"  # Replace with your .c or .txt file name

# Dictionary to hold character frequencies
char_freq = defaultdict(int)

try:
    with open(filename, 'r') as file:
        content = file.read()
        for char in content:
            char_freq[char] += 1

    # Display the frequencies
    print(f"Character frequencies in '{filename}':\n")
    for char, freq in sorted(char_freq.items()):
        if char == '\n':
            display_char = '\\n'
        elif char == '\t':
            display_char = '\\t'
        elif char == ' ':
            display_char = "' '"
        else:
            display_char = char
        print(f"{display_char}: {freq}")

except FileNotFoundError:
    print(f"File '{filename}' not found.")
