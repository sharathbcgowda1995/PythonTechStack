class FindMostCommonChar:
    key_value_dict = {}

    @staticmethod
    def most_common_char(word):
        # Count frequency of each character
        for char in word:
            if char not in FindMostCommonChar.key_value_dict:
                FindMostCommonChar.key_value_dict[char] = 1
            else:
                FindMostCommonChar.key_value_dict[char] += 1

        print(FindMostCommonChar.key_value_dict)  # Optional, to see the frequency of characters

        # Now find the most occurred character
        max_count = 0
        most_occured_char = ''

        for key, value in FindMostCommonChar.key_value_dict.items():
            if value > max_count:
                max_count = value
                most_occured_char = key

        return most_occured_char

# Test the class and method
word = 'Hello world !'
print(FindMostCommonChar.most_common_char(word))
