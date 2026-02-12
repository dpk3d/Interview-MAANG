"""
Find Maximum and Minimum Element in an Array

Problem: Given an array, find the maximum and minimum elements.

Approach 1: Using built-in functions - O(N) time, O(1) space
Approach 2: Linear scan - O(N) time, O(1) space
Approach 3: Sorting - O(N log N) time, O(1) space (not optimal)
Approach 4: Divide and Conquer - O(N) time, O(log N) space (recursive)
"""


def find_min_max_builtin(arr):
    """
    Find min and max using Python built-in functions.

    Time Complexity: O(N) - Two passes through array
    Space Complexity: O(1)

    Args:
        arr: Input array

    Returns:
        Tuple of (minimum, maximum)
    """
    if not arr:
        return None, None
    return min(arr), max(arr)


def find_min_max_linear(arr):
    """
    OPTIMAL SOLUTION - Find min and max using single linear scan.

    Time Complexity: O(N) - Single pass with 2 comparisons per element
    Space Complexity: O(1)

    Algorithm:
    1. Initialize min and max with first element
    2. Iterate through array comparing each element with current min/max
    3. Update min/max accordingly

    Args:
        arr: Input array

    Returns:
        Tuple of (minimum, maximum)
    """
    if not arr:
        return None, None

    minimum = maximum = arr[0]

    for num in arr[1:]:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return minimum, maximum


def find_min_max_sorting(arr):
    """
    Find min and max using sorting (NOT OPTIMAL).

    Time Complexity: O(N log N) - Due to sorting
    Space Complexity: O(1) - In-place sort

    Note: This is not optimal but included for comparison.

    Args:
        arr: Input array

    Returns:
        Tuple of (minimum, maximum)
    """
    if not arr:
        return None, None

    sorted_arr = sorted(arr)
    return sorted_arr[0], sorted_arr[-1]


def find_min_max_divide_conquer(arr, low, high):
    """
    Find min and max using Divide and Conquer approach.

    Time Complexity: O(N) - T(n) = 2T(n/2) + 2
    Space Complexity: O(log N) - Recursion stack

    Algorithm:
    1. Divide array into two halves
    2. Recursively find min/max in each half
    3. Combine results

    Comparison count: 3n/2 - 2 (better than linear scan's 2n comparisons)

    Args:
        arr: Input array
        low: Starting index
        high: Ending index

    Returns:
        Tuple of (minimum, maximum)
    """
    # Base case: Only one element
    if low == high:
        return arr[low], arr[low]

    # Base case: Two elements
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide and conquer
    mid = (low + high) // 2
    min1, max1 = find_min_max_divide_conquer(arr, low, mid)
    min2, max2 = find_min_max_divide_conquer(arr, mid + 1, high)

    return min(min1, min2), max(max1, max2)


# Test cases
if __name__ == "__main__":
    test_arr = [1, 23, 4, 5, -6, 5, 8, 34]

    # Approach 1: Built-in functions
    min_val, max_val = find_min_max_builtin(test_arr)
    print("Approach 1 (Built-in):")
    print(f"Min: {min_val}, Max: {max_val}")

    # Approach 2: Linear scan (OPTIMAL)
    min_val, max_val = find_min_max_linear(test_arr)
    print("\nApproach 2 (Linear Scan - OPTIMAL):")
    print(f"Min: {min_val}, Max: {max_val}")

    # Approach 3: Sorting (not optimal)
    min_val, max_val = find_min_max_sorting(test_arr)
    print("\nApproach 3 (Sorting):")
    print(f"Min: {min_val}, Max: {max_val}")

    # Approach 4: Divide and Conquer
    test_arr2 = [1020, 141, 45, 1, 90, 890]
    min_val, max_val = find_min_max_divide_conquer(test_arr2, 0, len(test_arr2) - 1)
    print("\nApproach 4 (Divide and Conquer):")
    print(f"Min: {min_val}, Max: {max_val}")
