"""
Trapping Rain Water Problem

Problem: Given an array arr[] of N non-negative integers representing the height of blocks.
If width of each block is 1, compute how much water can be trapped between the blocks
during the rainy season.

Example: arr = [3, 0, 0, 2, 0, 4]
Output: 10

Approach 1: Using auxiliary arrays to store left and right max heights
Time Complexity: O(N) - Three passes through the array
Space Complexity: O(N) - Two auxiliary arrays
"""


def trapping_water(arr):
    """
    Calculate trapped water using left and right max arrays.

    Algorithm:
    1. For each position, store the maximum height to its left
    2. For each position, store the maximum height to its right
    3. Water trapped at position i = min(left_max[i], right_max[i]) - arr[i]

    Args:
        arr: List of non-negative integers representing heights

    Returns:
        Total water trapped
    """
    if not arr or len(arr) < 3:
        return 0

    size = len(arr)
    left_max = [0] * size
    right_max = [0] * size
    trapped_water = 0

    # Build left_max array - maximum height to the left of each position
    left_max[0] = arr[0]
    for i in range(1, size):
        left_max[i] = max(left_max[i - 1], arr[i])

    # Build right_max array - maximum height to the right of each position
    right_max[size - 1] = arr[size - 1]
    for i in range(size - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], arr[i])

    # Calculate trapped water at each position
    for i in range(size):
        trapped_water += min(left_max[i], right_max[i]) - arr[i]

    return trapped_water


def trapping_water_optimal(arr):
    """
    OPTIMAL SOLUTION - Calculate trapped water using two pointers.

    Time Complexity: O(N) - Single pass through the array
    Space Complexity: O(1) - Only using constant extra space

    Algorithm (Two Pointer Approach):
    1. Use two pointers: left (start) and right (end)
    2. Track left_max and right_max heights seen so far
    3. Move the pointer with smaller height inward
    4. Water trapped = max_height - current_height (if current < max)

    Key Insight: Water level at any position is determined by the minimum of
    maximum heights on both sides. By using two pointers, we can calculate
    this in a single pass.

    Args:
        arr: List of non-negative integers representing heights

    Returns:
        Total water trapped
    """
    if not arr or len(arr) < 3:
        return 0

    left = 0
    right = len(arr) - 1
    left_max = 0
    right_max = 0
    trapped_water = 0

    while left <= right:
        if arr[left] <= arr[right]:
            # Process left side
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                trapped_water += left_max - arr[left]
            left += 1
        else:
            # Process right side
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                trapped_water += right_max - arr[right]
            right -= 1

    return trapped_water


# Test cases
if __name__ == "__main__":
    test_array = [3, 0, 0, 2, 0, 4]

    print("Approach 1 (Using auxiliary arrays):")
    print(f"Trapped Water: {trapping_water(test_array)}")

    print("\nApproach 2 (Optimal - Two Pointers):")
    print(f"Trapped Water: {trapping_water_optimal(test_array)}")

    # Expected Output: 10
