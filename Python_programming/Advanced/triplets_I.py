def find_triplet(arr, sum):
    arr.sort()  # Sorting the array

    for i in range(len(arr) - 2):
        low = i + 1
        high = len(arr) - 1

        while low < high:
            if arr[i] + arr[low] + arr[high] == sum:
                print(f"The triplet is {arr[i]}, {arr[low]}, {arr[high]}")
                return True
            elif arr[i] + arr[low] + arr[high] < sum:
                low += 1
            else:
                high -= 1

    # If no triplet is found
    return False

if __name__ == "__main__":
    arr = [12, 3, 4, 1, 6, 9]
    sum_value = 24

    if find_triplet(arr, sum_value) is False:
        print("No triplet found with the given sum.")
