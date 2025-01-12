def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# def bubble_sort(arr):
#     swap_counter = -1
#     while swap_counter != 0:
#         swap_counter = 0
#         for i in range(len(arr) - 1):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#                 swap_counter += 1

def bubble_sort(arr):
    for i in range(len(arr)-1,-1,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr

arr_num = [6, 5, 2, 1, 9, 10, 0]
print(arr_num)  # [6, 5, 2, 1, 9, 10, 0]
selection_sort(arr_num)
print(arr_num)  # [0, 1, 2, 5, 6, 9, 10]

arr_num = [6, 5, 2, 1, 9, 10, 0]
print(arr_num)  # [6, 5, 2, 1, 9, 10, 0]
bubble_sort(arr_num)
print(arr_num)  # [0, 1, 2, 5, 6, 9, 10]
