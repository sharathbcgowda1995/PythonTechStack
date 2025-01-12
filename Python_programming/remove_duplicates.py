class RemoveDuplicates():
    def remove_duplicates(self,string_value):
        result =""
        for char in string_value:
            if char not in result:
                result = result+char
        return result

word = "Programming"
obj = RemoveDuplicates()
print(obj.remove_duplicates(word))