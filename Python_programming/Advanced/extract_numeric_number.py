import re

# Input string
input_string = "abc38gh89"

# Use regular expression to find all numbers in the string
numbers = re.findall(r'\d+', input_string)

# Join the numbers to form the final result
result = ''.join(numbers)

print(result)  # Output: 3889