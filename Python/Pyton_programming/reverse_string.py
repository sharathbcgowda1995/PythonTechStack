class ReverseString():
    #Approach-1
    # def reverse_string(self,string_value):
    #     reversed_string = string_value[::-1]
    #     return reversed_string
    
    #Approach-2
    # def reverse_string(self,string_value):
    #     reverse_str = ""
    #     for char in string_value:
    #         print(char)
    #         reverse_str= char + reverse_str
    #     return reverse_str

    #Approach - 3
    def reverse_string(self,string_value):
        reverse_str = ""
        for char_ind in range(len(string_value) - 1, -1, -1):
            print(char_ind)
            reverse_str = reverse_str + string_value[char_ind]
        return reverse_str

string_value = "Sharath"
obj = ReverseString()
value = obj.reverse_string(string_value)
print("Before reversing :- %s and after the string reversed : %s "%(string_value,value))