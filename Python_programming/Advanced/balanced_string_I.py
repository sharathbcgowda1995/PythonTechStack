def is_balanced(str):
    opening_brackets = "({["
    closing_brackets = ")}]"
    stack = []

    for ch in str:
        if ch in opening_brackets:
            stack.append(ch)
        elif ch in closing_brackets:
            if not stack:
                return False

            latest_opened_par = stack.pop()

            if (
                (latest_opened_par == '(' and ch != ')')
                or (latest_opened_par == '{' and ch != '}')
                or (latest_opened_par == '[' and ch != ']')
            ):
                return False

    return len(stack) == 0

# Example usage:
print(is_balanced("[{()}]"))  # True
print(is_balanced("[({(})]"))  # False
print(is_balanced("{[}"))  # False
print(is_balanced("({}{}([{}]))"))  # True
print(is_balanced("({"))  # False