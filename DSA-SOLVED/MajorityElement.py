"""
Majority Element - Find elements appearing more than N/K times

Problem: Given an array of size n, find all elements that appear more than n/k times.

Example:
Input: arr = [3, 1, 2, 2, 1, 2, 3, 3], k = 4
Output: [2, 3]
Explanation: Array size is 8, so we need elements appearing more than 8/4 = 2 times.
Elements 2 and 3 both appear 3 times.

Approach 1: Using HashMap - O(N) time, O(N) space
Approach 2: Boyer-Moore Majority Vote (for k=3) - O(N) time, O(1) space
"""


def find_majority_elements_hashmap(arr, k):
    """
    Find elements appearing more than n/k times using HashMap.

    Time Complexity: O(N) - Single pass through array
    Space Complexity: O(N) - HashMap to store frequencies

    Algorithm:
    1. Count frequency of each element using HashMap
    2. Return elements with frequency > n/k

    Args:
        arr: Input array
        k: Divisor for threshold calculation

    Returns:
        List of elements appearing more than n/k times
    """
    if not arr or k <= 0:
        return []

    threshold = len(arr) // k
    frequency_map = {}

    # Count frequencies
    for num in arr:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    # Find elements exceeding threshold
    result = []
    for num, count in frequency_map.items():
        if count > threshold:
            result.append(num)

    return result


def find_majority_elements_boyer_moore(arr, k):
    """
    Find elements appearing more than n/k times using Boyer-Moore Majority Vote.

    Time Complexity: O(N) - Two passes through array
    Space Complexity: O(1) - Only storing k-1 candidates

    Note: This implementation works optimally for k=3 (finding elements > n/3).
    For general k, we need k-1 candidates, but this shows the concept for k=3.

    Algorithm (for k=3, finding elements appearing > n/3 times):
    1. At most 2 elements can appear more than n/3 times
    2. Use two candidate variables and their counts
    3. First pass: Find potential candidates
    4. Second pass: Verify candidates actually exceed threshold

    Args:
        arr: Input array
        k: Divisor for threshold calculation (optimized for k=3)

    Returns:
        List of elements appearing more than n/k times
    """
    if not arr:
        return []

    # Initialize two candidates and their counts
    count1, count2 = 0, 0
    candidate1, candidate2 = None, None

    # First pass: Find potential candidates
    for num in arr:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            # Decrement both counts (voting mechanism)
            count1 -= 1
            count2 -= 1

    # Second pass: Verify candidates
    threshold = len(arr) // k
    result = []
    for candidate in (candidate1, candidate2):
        if candidate is not None and arr.count(candidate) > threshold:
            result.append(candidate)

    return result


# Test cases
if __name__ == "__main__":
    # Test 1: HashMap approach
    arr1 = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
    k1 = 4
    print("Test 1 - HashMap Approach:")
    print(f"Array: {arr1}, k: {k1}")
    print(f"Elements appearing > n/k times: {find_majority_elements_hashmap(arr1, k1)}")

    # Test 2: Boyer-Moore approach (optimal for k=3)
    arr2 = [3, 1, 2, 2, 1, 2, 3, 3]
    k2 = 4
    print("\nTest 2 - Boyer-Moore Approach:")
    print(f"Array: {arr2}, k: {k2}")
    print(
        f"Elements appearing > n/k times: {find_majority_elements_boyer_moore(arr2, k2)}"
    )

    # Test 3: Finding elements appearing > n/3 times (ideal for Boyer-Moore)
    arr3 = [1, 1, 1, 2, 2, 2, 3, 3]
    k3 = 3
    print("\nTest 3 - Boyer-Moore for k=3:")
    print(f"Array: {arr3}, k: {k3}")
    print(
        f"Elements appearing > n/k times: {find_majority_elements_boyer_moore(arr3, k3)}"
    )
