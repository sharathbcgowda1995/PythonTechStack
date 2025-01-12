class SwapValues():
    def swap_variable_values(self,num1,num2):
        #Approach-1
        # num1,num2=num2,num1

        #Approach - 2
        # num1 = num1+num2
        # num2 = num1-num2
        # num1= num1-num2

        #Approah - 3
        temp = num1
        num1 = num2
        num2 = temp
        return num1,num2

num1=1
num2=2
obj = SwapValues()
num1,num2 = obj.swap_variable_values(num1,num2)
print(num1,num2)
