class SumOfTwo():
    @staticmethod
    def find_sum_of_two(array,sum):
        for i in range(len(array)):
            for j in range(i+1,len(array)):
                if arr[i]+arr[j]==sum:
                    print("Indexes are : %d , %d"%(i,j))
                    return arr[i],arr[j]
arr=[1, 2, 3, 5]
print(SumOfTwo.find_sum_of_two(arr,5))

