class Anagram():
    # Approach - 1
    # @staticmethod
    # def check_anagram_or_not(str1,str2):
    #     string1 = sorted(str1.replace(" ","").lower())
    #     string2 = sorted(str2.replace(" ","").lower())
    #     return string1==string2

    # Approach - 2 with extra details
    def check_anagram_or_not(str1,str2):
        string1 = sorted(str1.replace(" ","").lower())
        string2 = sorted(str2.replace(" ","").lower())
        print(string1,string2)

        string1_dict={}
        string2_dict={}

        if len(string1) != len(string2):
            return False

        else :
            for char in string1 :
                string1_dict[char]=string1.count(char)

            for char in string2:
                string2_dict[char]=string2.count(char)

            if string1_dict==string2_dict:
                print(string1_dict)
                print(string2_dict)
                return True
            else:
                return False

string1='listen12n'
string2='silennt12'
if(Anagram.check_anagram_or_not(string1,string2)):
    print('Both the strings are anagrams')
else:
    print('Both the strings are not the anagrams')