"""
https://www.programiz.com/java-programming/examples/check-valid-shuffle-of-strings

Given strings A, B, and C, find whether C is formed by an interleaving of A and B.

An interleaving of two strings S and T is a configuration such that it creates a new string Y from the concatenation substrings of A and B and |Y| = |A + B| = |C|

For example:

A = "XYZ"
B = "ABC"

We can make multiple interleaving string Y like, XYZABC, XAYBCZ, AXBYZC, XYAZBC and many more
so here your task is to check whether you can create a string Y which can be equal to C.

Specifically, you just need to create substrings of string A and create substrings B and
concatenate them and check whether it is equal to C or not.

Note: a + b is the concatenation of strings a and b.

Return true if C is formed by an interleaving of A and B, else return false.

Example 1:

Input:
A = YX, B = X, C = XXY
Output: 0
Explanation: XXY is not interleaving
of YX and X

Example 2:

Input:
A = XY, B = X, C = XXY
Output: 1
Explanation: XXY is interleaving of
XY and X.
"""


# concat and sort mechanism
# it's a simple solution does not work for all test cases..
def valid_shuffle(input_string1, input_string2, shuffle_string):
    concat_sort_str = sorted(input_string1 + input_string2)
    print(concat_sort_str)  # ['X', 'X', 'Y']
    sort_shuffle = sorted(shuffle_string)
    print(sort_shuffle)  # ['X', 'X', 'Y']
    if sort_shuffle == concat_sort_str:
        print(" It's a Valid shuffle string : " + shuffle_string)
        return True
    else:
        print(" Not valid shuffle string : " + shuffle_string)
        return False


str1 = "XY"
str2 = "X"
check_str = "XXY"
valid_shuffle(str1, str2, check_str)
# Output: It's a Valid shuffle string : XXY


def check_valid_shuffle(i, j, k, a, b, c, dp_array):
    if i == len(a) and j == len(b) and k == len(c):
        return 1

    if dp_array[i][j] != -1:
        return dp_array[i][j]

    out1, out2 = 0, 0

    if i < len(a) and a[i] == c[k]:
        out1 = check_valid_shuffle(i + 1, j, k + 1, a, b, c, dp_array)

    if j < len(b) and b[j] == c[k]:
        out2 = check_valid_shuffle(i, j + 1, k + 1, a, b, c, dp_array)
    dp_array[i][j] = out1 + out2
    print(dp_array[i][j])  # print 0 or 1, or 2
    return dp_array[i][j]


# Dynamic Programming
def is_interleave(a, b, c):
    j = 0
    i = 0
    k = 0
    dp_array = [[-1 for i in range(len(b) + 1)] for j in range(len(a) + 1)]
    print(dp_array)  # [[-1, -1], [-1, -1], [-1, -1]]
    if len(a) + len(b) != len(c):
        return 0
    print(check_valid_shuffle(i, j, k, a, b, c, dp_array))  # print 0 or 1
    return check_valid_shuffle(i, j, k, a, b, c, dp_array)


str1 = "YX"
str2 = "X"
check_str = "XXY"
is_interleave(str1, str2, check_str)
# Output: 0
