
#array and different methods

array = [1, 2, 3, 4, 5]
print("Array:", array)

print("Element at index 2:", array[2])

array.append(6)
print("Array after appending 6:", array) #add element at last

array.insert(2, 10)
print("Array after inserting at index 2:", array)

array.remove(4)
print("Array after removing 4:", array)

index = array.index(3)
print("Index of 3:", index)

pop = array.pop(5)
print ("Array after poping element at 5:", pop)

print(array)  