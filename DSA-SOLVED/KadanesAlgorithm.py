"""
Kadane's Algorithm - Find the contiguous sub-array with maximum sum.

Problem: Given an array arr of N integers, find the contiguous sub-array with maximum sum.

Time Complexity: O(N) - Single pass through the array
Space Complexity: O(1) - Only using constant extra space

Algorithm:
1. Keep track of current sum and maximum sum found so far
2. Add each element to current sum
3. If current sum becomes negative, reset it to 0 (start fresh from next element)
4. Update maximum sum whenever current sum exceeds it
"""


def maximum_sum_sub_array(arr):
    """
    Find maximum sum of contiguous subarray using Kadane's Algorithm.

    Args:
        arr: List of integers

    Returns:
        Tuple of (max_sum, start_index, end_index)
    """
    if not arr:
        return 0, -1, -1

    size = len(arr)
    current_sum = 0
    maximum_sum_so_far = arr[0]
    start_index = 0
    end_index = 0
    temp_start = 0  # Temporary start position for current window

    for i in range(size):
        current_sum += arr[i]

        # Update maximum sum and indices if current sum is greater
        if current_sum > maximum_sum_so_far:
            maximum_sum_so_far = current_sum
            start_index = temp_start
            end_index = i

        # Reset current sum if it becomes negative
        # Start fresh from next element
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return maximum_sum_so_far, start_index, end_index


# Test case
if __name__ == "__main__":
    array = [3, 4, -5, 3, -4, -4, 8, 3, -2, 7, -10]
    max_sum, start, end = maximum_sum_sub_array(array)

    print(f"Maximum Sum Subarray: {max_sum}")
    print(f"Start Index: {start}")
    print(f"End Index: {end}")
    print(f"Subarray: {array[start:end+1]}")

    """
    Expected Output:
    Maximum Sum Subarray: 16
    Start Index: 6
    End Index: 9
    Subarray: [8, 3, -2, 7]
    """
