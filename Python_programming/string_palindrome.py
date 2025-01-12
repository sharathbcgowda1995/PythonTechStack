class StringPalindrome():
    @staticmethod
    def palindrome_or_not(string_value):

        # Apporoach-1
        #reversed_string = string_value[::-1]
        string_value_reversed = ""

        # Apporoach-2
        for char in string_value:
            string_value_reversed = char+string_value_reversed
        if (string_value==string_value_reversed):
            print("Palindrome string")
        else:
            print("Not palindrome string")

        #Apporoach-3
        # for index in range(len(string_value)-1,-1,-1):#we have to use like this  -1 so that it will iterate till 0
        #     string_value_reversed += string_value[index]
        # print(string_value_reversed)
        #
        # if (string_value==string_value_reversed):
        #     print("Palindrome string")
        # else:
        #     print("Not palindrome string")



string_val = "scs"
StringPalindrome.palindrome_or_not(string_val)