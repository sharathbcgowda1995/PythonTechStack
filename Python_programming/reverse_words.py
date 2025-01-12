class ReveseWords():
    # Approach -1
    @staticmethod
    def reverse_words(string_words):
        arr = string_words.split(" ")
        reversed_string=""
        for index in range(len(arr)-1,-1,-1):
            reversed_string= reversed_string + arr[index] + " "
        return reversed_string

    #Approach -2
    # @staticmethod
    # def reverse_words(string_words):
    #     string_arr = string_words.split(' ')
    #     reversed_arr = string_arr[::-1]
    #     reversed_string = ' '.join(reversed_arr)
    #     return  reversed_string

original_string = 'My name is Sharath'
reversed_string_value = ReveseWords.reverse_words(original_string)
print("Reversed string is : %s"%(reversed_string_value))
