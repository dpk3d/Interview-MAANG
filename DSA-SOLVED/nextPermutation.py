"""
Next Permutation

Problem: Find the next lexicographically greater permutation of an array.
If no such permutation exists, rearrange to the lowest possible order (sorted).

Examples:
- [1,2,3] -> [1,3,2]
- [2,3,1] -> [3,1,2]
- [3,2,1] -> [1,2,3] (no greater permutation exists, so return smallest)

Constraint: Must be done in-place with O(1) extra space.

Algorithm:
1. Find the largest index i such that nums[i] < nums[i+1]
   (This is the "pivot" - rightmost position where we can increase)
2. If no such index exists, array is in descending order (largest permutation)
   -> Reverse entire array to get smallest permutation
3. Find the largest index j > i such that nums[i] < nums[j]
   (Find smallest element greater than pivot to swap with)
4. Swap nums[i] and nums[j]
5. Reverse the suffix starting at nums[i+1]
   (Make the suffix as small as possible)

Time Complexity: O(N)
Space Complexity: O(1)
"""


def next_permutation(nums):
    """
    Find next lexicographically greater permutation in-place.

    Args:
        nums: List of integers (modified in-place)

    Returns:
        Modified nums array (also modifies in-place)
    """
    if not nums or len(nums) <= 1:
        return nums

    n = len(nums)

    # Step 1: Find the pivot (rightmost position where nums[i] < nums[i+1])
    pivot = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break

    # Step 2: If no pivot found, array is in descending order
    # Reverse to get smallest permutation
    if pivot == -1:
        nums.reverse()
        return nums

    # Step 3: Find the smallest element greater than nums[pivot] to swap with
    # Search from right to left for efficiency
    swap_idx = n - 1
    while nums[swap_idx] <= nums[pivot]:
        swap_idx -= 1

    # Step 4: Swap pivot with the found element
    nums[pivot], nums[swap_idx] = nums[swap_idx], nums[pivot]

    # Step 5: Reverse the suffix after pivot to make it smallest
    # This gives us the next permutation
    nums[pivot + 1 :] = reversed(nums[pivot + 1 :])

    return nums


# Test cases
if __name__ == "__main__":
    # Test 1: Normal case
    arr1 = [1, 3, 5, 4, 3, 2, 1]
    print(f"Original: {arr1}")
    result1 = next_permutation(arr1.copy())
    print(f"Next Permutation: {result1}")

    # Test 2: Simple case
    arr2 = [1, 2, 3]
    print(f"\nOriginal: {arr2}")
    result2 = next_permutation(arr2.copy())
    print(f"Next Permutation: {result2}")

    # Test 3: Largest permutation (should wrap to smallest)
    arr3 = [3, 2, 1]
    print(f"\nOriginal: {arr3}")
    result3 = next_permutation(arr3.copy())
    print(f"Next Permutation: {result3}")

    # Test 4: Another case
    arr4 = [2, 3, 1]
    print(f"\nOriginal: {arr4}")
    result4 = next_permutation(arr4.copy())
    print(f"Next Permutation: {result4}")
