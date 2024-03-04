# For Loop
for i in range(5):  
    print(i)
print()

# While Loop
j = 0
while j < 5:
    print(j)
    j += 1
print()

# Nested Loops
for x in range(3):
    for y in range(2):
        print(f'({x}, {y})')
print()

# Loop Control Statements
# Break
print("Using Break:")
for i in range(10):
    if i == 5:
        break
    print(i)
print()

# Continue
print("Using Continue:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
print()


# For Loop with Else
for i in range(5):
    print(i)
else:
    print("Loop completed successfully!")

# While Loop with Else
k = 0
while k < 5:
    print(k)
    k += 1
else:
    print("While Loop completed successfully!")
print()

# Looping Through Lists
my_list = ["apple", "banana", "cherry"]
for item in my_list:
    print(item)
print()

# Looping Through Dictionaries
my_dict = {"name": "John", "age": 30, "city": "New York"}
for key, value in my_dict.items():
    print(key, ":", value)
print()

# Looping Through Strings
my_string = "Hello"
for char in my_string:
    print(char)
print()

# Looping Through Tuples
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item)
print()