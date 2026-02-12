"""
Sort Array of 0s, 1s, and 2s (Dutch National Flag Problem)

Problem: Given an array of size N containing only 0s, 1s, and 2s,
sort the array in ascending order.

This is also known as the Dutch National Flag problem.

Approach 1: Dutch National Flag Algorithm (Three-way partitioning)
Time Complexity: O(N) - Single pass
Space Complexity: O(1) - In-place sorting

Approach 2: Counting Sort
Time Complexity: O(N) - Two passes
Space Complexity: O(1) - Only counting variables
"""


def sort_dutch_flag(arr):
    """
    OPTIMAL SOLUTION - Sort using Dutch National Flag algorithm.

    Algorithm:
    - Use three pointers: low, mid, high
    - low: boundary for 0s (elements before low are 0s)
    - mid: current element being examined
    - high: boundary for 2s (elements after high are 2s)

    Process:
    - If arr[mid] == 0: swap with low, increment both low and mid
    - If arr[mid] == 1: just increment mid
    - If arr[mid] == 2: swap with high, decrement high

    Args:
        arr: List containing only 0s, 1s, and 2s

    Returns:
        Sorted array (in-place)
    """
    if not arr:
        return arr

    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            # Swap with low boundary and move both pointers forward
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # 1 is in correct position, just move mid forward
            mid += 1
        else:  # arr[mid] == 2
            # Swap with high boundary and move high pointer backward
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


def sort_counting(arr):
    """
    Alternative approach using counting sort.

    Algorithm:
    1. Count occurrences of 0s, 1s, and 2s
    2. Overwrite array with counted values in order

    Time Complexity: O(N) - Two passes
    Space Complexity: O(1) - Only three counter variables

    Args:
        arr: List containing only 0s, 1s, and 2s

    Returns:
        Sorted array (in-place)
    """
    if not arr:
        return arr

    # Count occurrences
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for num in arr:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        elif num == 2:
            count_2 += 1

    # Overwrite array with sorted values
    index = 0

    # Fill 0s
    while count_0 > 0:
        arr[index] = 0
        index += 1
        count_0 -= 1

    # Fill 1s
    while count_1 > 0:
        arr[index] = 1
        index += 1
        count_1 -= 1

    # Fill 2s
    while count_2 > 0:
        arr[index] = 2
        index += 1
        count_2 -= 1

    return arr


# Test cases
if __name__ == "__main__":
    test_arr_1 = [0, 1, 2, 0, 1, 2, 0, 1, 2, 1, 2, 0, 1, 2]
    print("Original array:", test_arr_1)
    print("Sorted (Dutch Flag):", sort_dutch_flag(test_arr_1.copy()))

    test_arr_2 = [0, 1, 2, 0, 1, 2, 0, 1, 2, 1, 2, 0, 1, 2]
    print("Sorted (Counting):", sort_counting(test_arr_2))

    """
    Expected Output:
    Sorted array: [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    """
