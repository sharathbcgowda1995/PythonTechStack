class Kadanes_Algorithm():
    def find_maximum(self,array):
        current_sum = 0
        max_sum =0
        for i in range(len(array)):
            current_sum=current_sum+array[i]
            if (current_sum > max_sum):
                max_sum=current_sum
            if (current_sum<0):
                current_sum=0
        return max_sum

obj = Kadanes_Algorithm()
#array = [-2,1,-3,4,-1,2,1,-5,4]
array = [5,4,-1,7,8]
print("maximum sum from the sub array is : ", obj.find_maximum(array))