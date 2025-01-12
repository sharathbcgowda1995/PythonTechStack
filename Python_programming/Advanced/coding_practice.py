def selection_sort(array):
    for i in range(len(array)):
        min_index=i
        for j in range(i+1,len(array)):
            if array[j] < array[min_index]:
                min_index=j
            array[i],array[min_index]=array[min_index],array[i]
    return  array

def bubble_sort(array):
    for i in range(len(array)):
        if array[i]< array[i+1]:
            array[i],array[i+1]=array[i+1],array[i]
        return array

arr_num = [6, 5, 2, 1, 9, 10, 0]
#print(selection_sort(arr_num))
print(bubble_sort(arr_num))