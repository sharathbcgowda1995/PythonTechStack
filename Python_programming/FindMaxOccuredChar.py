arr = []
def get_the_most_repeating_charatcter(word):
    dict = {}
    for char in word:
        dict[char] = word.count(char)
    # print(dict)

    max_rept_char = ''
    max = 0

    arr = []
    for i in dict.values():
        arr.append(i)
        # print(arr)
    # print(arr)

    for i in arr:
        if i > max :
            max = i

    # print(f"maximum is :{max} ")

    for value in dict.keys():
        if dict[value] == max :
            # print(value)
            max_rept_char = value
            # print (max)
    return (max_rept_char)


word = 'Hello world'
print(get_the_most_repeating_charatcter(word))