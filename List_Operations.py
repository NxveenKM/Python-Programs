# Simple List Demonstration

# Create a list of fruits
fruits = ["apple", "banana", "cherry"]

# Print the original list
print("Original list of fruits:", fruits)

# Add a fruit to the list
fruits.append("date")
print("After adding 'date':", fruits)

# Remove a fruit from the list
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Access and print the first fruit
print("First fruit in the list:", fruits[0])

# Loop through the list and print each fruit
print("All fruits in the list:")
for fruit in fruits:
    print(fruit)
