"""

https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

"""
from collections import defaultdict


# Using Map
# Time Complexity: O(nlogn)
# Space complexity: O(k), k= size of map
def print_duplicate(input_string):
    char_map = defaultdict(int)
    for x in range(len(input_string)):
        char_map[input_string[x]] += 1
    for char in char_map:
        if char_map[char] > 1:
            print(char, ", count = ", char_map[char])


test_str = 'deepppaaakkkkk'
print_duplicate(test_str)
# Output: p , count =  3
#         a , count =  3
#         k , count =  5


# Using Stack
# Time Complexity : O(n)
# Space Complexity: O(n)
def remove_duplicate(input_string):
    stack = []
    last_occurance = {char: x for x, char in enumerate(input_string)}
    print(last_occurance)
    # {'s': 2, 'i': 5, 'n': 6, 'g': 7, 'h': 8}

    for x, char in enumerate(input_string):
        if char in stack:
            continue
        while stack and char < stack[-1] and x < last_occurance[stack[-1]]:
            stack.pop()
        stack.append(char)
    print(''.join(stack))
    # singh
    return ''.join(stack)


test_str = 'sssiiingh'
remove_duplicate(test_str)
# Output: singh
