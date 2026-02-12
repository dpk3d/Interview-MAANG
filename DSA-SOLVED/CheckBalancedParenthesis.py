"""
Given below parenthesis, print them as true if they are valid/balanced else false.

(()). —> True
)(()) -> False
(()())   -> True
)()-> False

"""


# Time Complexity O(N), Space Complexity O(1)
def check_balanced(expression):
    flag = True
    count = 0

    for x in range(len(expression)):
        if expression[x] == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            flag = False
            break
    if count != 0:
        flag = False
    return flag


# Example usage
print(check_balanced("(())"))  # Output: True
print(check_balanced(")(())"))  # Output: False
print(check_balanced("(()())"))  # Output: True
print(check_balanced(")("))  # Output: False


# Using Stacks
def is_balanced(input_str: str) -> bool:
    bracket_dict = {")": "(", "]": "[", "}": "{"}
    stack = [0]

    for char in input_str:
        if char in bracket_dict.values():
            stack.append(char)
        elif dict[char] != stack.pop():
            return False

    return len(stack) == 1
