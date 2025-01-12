def rotate_array(arr, k):
    # Perform rotation k times
    for i in range(k):
        # Remove the last element and insert it at the beginning
        last_element = arr.pop()
        arr.insert(0, last_element)

# Given array
array = [1, 2, 3, 4, 5, 6, 7]

# Rotate the array 3 times
rotate_array(array, 3)

# Print the rotated array
print("Rotated array:", array)
