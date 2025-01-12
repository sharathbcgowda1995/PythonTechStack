s = "this1 new4 string5 is2 a3"

# Custom sorting function to sort words based on numeric values
def custom_sort(words):
    n = len(words)
    for i in range(n):
        for j in range(0, n-i-1):
            if get_number(words[j]) > get_number(words[j+1]):
                words[j], words[j+1] = words[j+1], words[j]

# Function to extract the numeric part from a word
def get_number(word):
    num = 0
    for char in word:
        if char.isdigit():
            num = num * 10 + int(char)
    return num

# Convert string to list of words
words = s.split()

# Sort the words using custom_sort function
custom_sort(words)

# Join the sorted words back into a string
sorted_string = ' '.join(words)

print(sorted_string)
