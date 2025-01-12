def to_lowercase(input_string):
    result = ''  # Start with an empty string to store the result

    # Loop through each character in the input string
    for char in input_string:
        # Check if the character is an uppercase letter (A-Z)
        if 'A' <= char <= 'Z':
            # Convert it to lowercase by adding 32 to its ASCII value
            result += chr(ord(char) + 32)
        else:
            # If it's not an uppercase letter, just add it as is
            result += char

    return result


# Example usage
input_string = "Hello 234 World!"
lowercase_string = to_lowercase(input_string)
print(lowercase_string)  # Output: hello world!
