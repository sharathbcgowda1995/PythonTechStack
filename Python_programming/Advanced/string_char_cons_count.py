def string_concatenation(input_string):
    result = ""  # To store the final result
    i = 0  # Pointer to go through the string

    while i < len(input_string):
        char = input_string[i]  # Current character
        count = 1  # Start with count 1

        # Count the number of consecutive same characters
        while i + 1 < len(input_string) and input_string[i + 1] == char:
            count += 1
            i += 1

        # Add the character and its count (only if count > 1)
        result += char + (str(count) if count > 1 else '')

        i += 1  # Move to the next new character

    return result


# Example usage:
input_string = "aaabbbacfwww"
output_string = string_concatenation(input_string)
print(output_string)  # Output: a3b3acfw3
