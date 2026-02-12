"""
Merge Two Sorted Arrays

Problem: Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order.
Merge them in sorted order.

Approach 1: Using extra space - O(N+M) time, O(N+M) space
Approach 2: In-place using insertion - O(N*M) time, O(1) space
Approach 3: Gap Algorithm (Shell Sort) - O((N+M)*log(N+M)) time, O(1) space - OPTIMAL
"""


def merge_two_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays using extra space.

    Time Complexity: O(N + M) where N and M are lengths of arrays
    Space Complexity: O(N + M) for the result array

    Algorithm:
    1. Use two pointers, one for each array
    2. Compare elements and add smaller one to result
    3. Add remaining elements from non-empty array

    Args:
        arr1: First sorted array
        arr2: Second sorted array

    Returns:
        Merged sorted array
    """
    if not arr1:
        return arr2.copy()
    if not arr2:
        return arr1.copy()

    i = 0
    j = 0
    result = []

    # Merge while both arrays have elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Add remaining elements from arr1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    # Add remaining elements from arr2
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


def merge_inplace_insertion(arr1, arr2):
    """
    Merge two sorted arrays in-place using insertion approach.

    Time Complexity: O(N * M) where N and M are lengths of arrays
    Space Complexity: O(1) - In-place modification

    Algorithm:
    1. For each element in arr1, compare with first element of arr2
    2. If arr1[i] > arr2[0], swap them
    3. After swap, insert arr2[0] at correct position in arr2 (like insertion sort)
    4. This ensures arr1 has smallest N elements and arr2 has largest M elements

    Args:
        arr1: First sorted array (will contain smallest elements after merge)
        arr2: Second sorted array (will contain largest elements after merge)

    Note: Modifies both arrays in-place
    """
    if not arr1 or not arr2:
        return

    n = len(arr1)
    m = len(arr2)

    for i in range(n):
        # If current element of arr1 is greater than first element of arr2
        if arr1[i] > arr2[0]:
            # Swap them
            arr1[i], arr2[0] = arr2[0], arr1[i]

            # Place arr2[0] at correct position in arr2 using insertion sort
            first = arr2[0]
            j = 1
            while j < m and arr2[j] < first:
                arr2[j - 1] = arr2[j]
                j += 1
            arr2[j - 1] = first


def calculate_gap(length):
    """
    Calculate gap for shell sort based merging.
    Gap starts at ceil(length/2) and reduces by half each iteration.

    Args:
        length: Total length

    Returns:
        Next gap value (0 when done)
    """
    if length <= 1:
        return 0
    return (length // 2) + (length % 2)


def merge_gap_algorithm(arr1, arr2):
    """
    OPTIMAL SOLUTION - Merge using Gap Algorithm (Shell Sort approach).

    Time Complexity: O((N+M) * log(N+M))
    Space Complexity: O(1) - In-place modification

    Algorithm (Gap Method):
    1. Start with gap = ceil((n+m)/2)
    2. Compare elements at distance 'gap' and swap if needed
    3. Reduce gap by half and repeat until gap becomes 0
    4. This works across both arrays treating them as one virtual array

    This is the most optimal solution for merging in-place.

    Args:
        arr1: First sorted array (will contain smallest elements after merge)
        arr2: Second sorted array (will contain largest elements after merge)

    Note: Modifies both arrays in-place
    Reference: Based on Shell Sort algorithm
    """
    if not arr1 or not arr2:
        return

    n = len(arr1)
    m = len(arr2)
    total_length = n + m
    gap = calculate_gap(total_length)

    while gap > 0:
        i = 0

        # Compare elements in arr1
        while i + gap < n:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1

        # Compare elements between arr1 and arr2
        j = max(0, gap - n)  # Starting position in arr2
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        # Compare elements in arr2
        if j < m:
            j = 0
            while j + gap < m:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1

        gap = calculate_gap(gap)


# Test cases
if __name__ == "__main__":
    # Test 1: Basic merge with extra space
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4, 8, 10, 12]
    result = merge_two_sorted_arrays(arr1, arr2)
    print("Approach 1 (Extra Space):")
    print(f"Merged Array: {result}")

    # Test 2: In-place merge using insertion
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4, 6]
    merge_inplace_insertion(arr1, arr2)
    print("\nApproach 2 (In-place Insertion):")
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print(f"Combined: {arr1 + arr2}")

    # Test 3: Optimal gap algorithm
    arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    arr2 = [2, 4, 6, 8]
    merge_gap_algorithm(arr1, arr2)
    print("\nApproach 3 (Gap Algorithm - OPTIMAL):")
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print(f"Combined: {arr1 + arr2}")
