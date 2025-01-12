def move_zeros_ones(arr):
    n = len(arr)

    # Two pointers approach:
    # - one pointer (left) to fill zeros at the beginning
    # - another pointer (right) to fill ones at the end
    left = 0
    right = n - 1

    i = 0
    while i <= right:
        if arr[i] == 0:
            # Move zero to the left side
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
        elif arr[i] == 1:
            # Move one to the right side
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
            i -= 1  # To recheck the swapped element
        # Move to the next element
        i += 1

    return arr


# Example usage:
arr = [3, 0, 4, 1, 2, 0, 1, 5]
result = move_zeros_ones(arr)
print(result)  # Output: [0, 0, 4, 2, 3, 5, 1, 1]
