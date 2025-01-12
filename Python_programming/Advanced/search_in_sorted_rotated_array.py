class sorted_rotated_array:
    def search_in_sorted_rotated_array(self, array, element):
        low = 0
        high = len(array) - 1  # Corrected to avoid out-of-bounds access
        while (low <= high):
            mid = (low + high) // 2  # Ensure mid is an integer
            if element == array[mid]:
                return mid
            if array[low] <= array[mid]:
                if (element >= array[low] and element < array[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if element > array[mid] and element <= array[high]:
                    low = mid + 1
                else:
                    high = mid - 1  # Corrected to avoid infinite loop
        return -1  # Element not found


obj = sorted_rotated_array()
array = [5, 10, 11, 12, 1, 2, 3, 4]
element = 12
print(obj.search_in_sorted_rotated_array(array, element))
