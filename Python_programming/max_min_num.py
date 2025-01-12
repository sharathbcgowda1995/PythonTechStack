class MaxMin():
    @staticmethod
    def find_max_and_minimum_number(array):
        if len(array) >= 1:
            min = float('inf')
            max = float('-inf')

            for value in array:
                if value < min :
                    min = value

                if value > max :
                    max = value

            print("Maximum value in the array is : %d"%(max))
            print("Minimum value in the array is : %d" % (min))
        else:
            print("Empty array")

number_array = [1,3,5]
MaxMin.find_max_and_minimum_number(number_array)
