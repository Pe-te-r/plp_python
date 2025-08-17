# Create an empty list
my_list = []

# Append elements
my_list.extend([10, 20, 30, 40]) 
print("After appending:", my_list)  # [10, 20, 30, 40]

# Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)
print("After inserting 15:", my_list) 

# Extend my_list with another list
my_list.extend([50, 60, 70])
print("After extending:", my_list)

# Remove the last element from my_list
my_list.pop()
print("After removing last element:", my_list)

# Sort my_list in ascending order
my_list.sort()
print("After sorting:", my_list)

# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)