"""
https://leetcode.com/problems/add-digits/description/
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.



Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0



Constraints:

    0 <= num <= 231 - 1

"""


def add_digits_till_end(number):
    total_sum = 0
    while number > 0:
        reminder = number % 10
        total_sum += reminder
        number = number // 10
    if total_sum > 9:
        total_sum = add_digits_till_end(total_sum)
    return total_sum


print(add_digits_till_end(143))
# Output: 8
