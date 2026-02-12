"""
https://leetcode.com/problems/count-and-say/

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit.
Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":

Given a positive integer n, return the nth term of the count-and-say sequence.


Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

"""

from itertools import groupby


# Time Complexity : O(N * M)
# Space Complexity : O(N * M)
def count_and_say(n):
    if n == 1:
        return "1"
    if n == 2:
        return "11"
    start_string = "11"
    for x in range(2, n):
        count = 1
        new_string = ""
        for y in range(len(start_string)):
            if y == len(start_string) - 1:
                new_string = new_string + str(count) + start_string[y]
                break
            if start_string[y] == start_string[y + 1]:
                count += 1
            else:
                new_string = new_string + str(count) + start_string[y]
                count = 1
        start_string = new_string
    return new_string


print("Generated String is : ", count_and_say(6))
# Output: Generated String is :  312211


# Time Complexity : O(N * N)
def count_and_say_recursive(n):
    if n == 1:
        return "1"
    last = count_and_say_recursive(n - 1)
    n = len(last)
    result = ""
    count = 1
    for x in range(n):
        if x == n - 1 or last[x] != last[x + 1]:
            result += str(count) + last[x]
            count = 1
        else:
            count += 1

    return result


print("Generated String via Recursive approach : ", count_and_say_recursive(6))
# Output: Generated String via Recursive approach :  312211


#     Time:   O(2^n)
#     Memory: O(2^n)
def count_and_say_elegant(n):
    if n == 1:
        return "1"
    return get_count(count_and_say_elegant(n - 1))


def get_count(n):
    return "".join(f"{sum(1 for _ in group)}{key}" for key, group in groupby(n))


print("Generated String via Elegant Recursive approach : ", count_and_say_elegant(6))
# Output: Generated String via Elegant Recursive approach :  312211


def count_and_say_dp(n):
    dynamic_program = ["" for x in range(0, n + 1)]
    dynamic_program[1] = "1 "
    x = 2
    while x < n + 1:
        print(f"x:{x} dynamic_program[{x - 1}]:{dynamic_program[x - 1]}")
        # x:2 dynamic_program[1]:1
        # x:3 dynamic_program[2]:11
        # x:4 dynamic_program[3]:21
        # x:5 dynamic_program[4]:1211
        # x:6 dynamic_program[5]:111221
        # x:7 dynamic_program[6]:312211
        # x:8 dynamic_program[7]:13112221
        # x:9 dynamic_program[8]:1113213211
        count = 0
        for y in range(0, len(dynamic_program[x - 1]) - 1):
            if dynamic_program[x - 1][y] == dynamic_program[x - 1][y + 1]:
                count += 1
            else:
                dynamic_program[x] += (
                    chr(count + 1 + ord("0")) + dynamic_program[x - 1][y]
                )
                count = 0
        dynamic_program[x] += " "
        x += 1
    return dynamic_program[-1][:-1]


print("Generated String via DP approach : ", count_and_say_dp(9))
# Output: Generated String via DP approach :  31131211131221
