"""
Given an array of binary digits, 0 and 1, sort the array so that all 0 are at one end and
all the 1 are at other end, which end doesn't matter. To sort the array swap any two adjacent
elements. Determine the minimum Number of swap to sort the array.

Example:
    arr=[0,1,0,1] -> with one move switching element 1 and 2 yields [0,0,1,1]

Complete the function minMoves below.

minMoves has following parameters :
int arr[n] : An array of binary digits

Return : Minimum number of moves required.

"""


def min_moves(arr):
    count = 0
    num_of_unplaced_zero = 0

    for moves in range(len(arr)):
        if arr[moves] == 0:
            num_of_unplaced_zero += 1
        else:
            count += num_of_unplaced_zero
    return count


digits = [1, 1, 1, 1, 0, 1, 0, 1]
print("Minimum Number of moves required to sort array is", min_moves(digits))
# Output: Minimum Number of moves required to sort array is 3
# This is not optimal solution but passes 12 test case out of 13.
