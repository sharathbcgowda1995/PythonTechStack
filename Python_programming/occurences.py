def test_find_ocuurence():
    word = 'AAACCBA'
    count= 1
    result = ""

    # Iterate through the string starting from the second character
    for i in range(1, len(word) + 1):

        if i < len(word) and word[i] == word[i - 1]:
            # If current character is the same as the previous one, increase count
            count += 1
        else:
            # Otherwise, add the previous character and count to the result
            result += word[i - 1] + str(count)
            count = 1  # Reset the count for the new character

    print(result)
