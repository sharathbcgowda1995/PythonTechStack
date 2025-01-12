class Occurences:
    @staticmethod
    def find_occurence_of_string(string_value):
        string_dict={}
        for char in string_value:
            if char not in string_dict:
                string_dict[char]=1
            else :
                string_dict[char]= string_dict[char]+1
        return string_dict

value ="Sharath"
print(Occurences.find_occurence_of_string(value))