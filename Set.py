# Using curly braces
my_set = {1, 2, 3}

# Using set() constructor
my_set = set([1, 2, 3])

# Check if an element exists
print(2 in my_set)  # True

# Loop through set
for item in my_set:
    print(item)
    
# Add an element
my_set.add(4)

# Add multiple elements
my_set.update([5, 6])

# Remove an element (raises error if not found)
my_set.remove(2)

# Remove an element (no error if not found)
my_set.discard(10)

# Remove and return an arbitrary element could be any number
element = my_set.pop()

# Clear the set
my_set.clear()

del my_set  # Deletes the set object entirely

a = {1, 2, 3}
b = {3, 4, 5}

# Union
print(a | b)  # {1, 2, 3, 4, 5}

# Intersection
print(a & b)  # {3}

# Difference
print(a - b)  # {1, 2}

# Symmetric Difference
print(a ^ b)  # {1, 2, 4, 5}