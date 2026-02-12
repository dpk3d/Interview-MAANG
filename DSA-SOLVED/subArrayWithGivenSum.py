"""
Given an unsorted array A of size N that contains only non-negative integers,
find a continuous sub-array which adds to a given number S.
If not found then return Empty [].
"""

array = [4, 7, 8, 7, 2, 4, 3, 7]


def get_sub_array_with_given_sum(arr, s):
    result = []
    for x in range(len(arr)):
        result.append(arr[x])
        while sum(result) > s:
            result.pop(0)
        if sum(result) == s:
            return result
    return []


print(get_sub_array_with_given_sum(array, 17))
# Output: [7, 8, 2]
