class ReverseArray():
    #Approach-1
    # def reverse_array(self,array):
    #     reversed_array= array[::-1]
    #     return reversed_array

    # Approach-2
    def reverse_array(self, array):
        left,right = 0,len(array)-1
        while(left<right):
            array[left],array[right]=array[right],array[left]
            left += 1
            right -= 1
        return array

    # Approach-3
    # def reverse_array(self, array):
    #     reversed_arr = []
    #     for index in range(len(array)-1,-1,-1):
    #         print(array[index])
    #         reversed_arr.append(array[index])
    #     return reversed_arr

obj = ReverseArray()
original_arr = [1,2,3,4,5]
array_reversed = obj.reverse_array(original_arr)
print("Array reversed is : %s "%(array_reversed))