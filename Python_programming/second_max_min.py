class SecondMaxMin:
    @staticmethod
    def get_second_highest_lowest_number(array):
        if len(array) > 2:
            first_min = second_min = float('inf')
            first_max = second_max = float('-inf')

            for value in array:
                if value < first_min:
                    second_min = first_min
                    first_min = value
                elif value < second_min and value != first_min:
                    second_min = value

                if value > first_max:
                    second_max = first_max
                    first_max = value
                elif value > second_max and value != first_max:
                    second_max = value

            return second_min, second_max

        else:
            print("Array has less than two elements to get the second-highest and second-lowest numbers.")

array = [1, 2, 3, 4]
second_minimum, second_maximum = SecondMaxMin.get_second_highest_lowest_number(array)
print("Second minimum number is: %d, Second maximum number is: %d" % (second_minimum, second_maximum))
