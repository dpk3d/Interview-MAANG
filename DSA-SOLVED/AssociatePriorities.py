# Hacker Rank Priorities Input is [1, 3, 7, 3] and Output should be [1, 2, 3, 2]
# Another Input is [2, 9, 3, 3, 3] and Output is [1, 3, 2, 1, 2]


def priorities(input_arr):
    temp = sorted(set(input_arr))
    ans = []
    for each in input_arr:
        ans.append((temp.index(each) + 1))
    print(ans)


if __name__ == "__main__":
    input_arr = [2, 9, 3, 2, 3]
    print(input_arr)
    priorities(input_arr)
    # Output: [2, 9, 3, 2, 3]
    # [1, 3, 2, 1, 2]
