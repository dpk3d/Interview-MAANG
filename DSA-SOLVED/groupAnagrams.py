"""
Given an array of strings 'arr', group the anagrams together.

Input: arr = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""

from typing import List


def group_anagrams(arr):
    anagram_dict = {}
    for word in arr:
        sort_word = "".join(sorted(word))
        if sort_word in anagram_dict:
            anagram_dict[sort_word].append(word)
        else:
            anagram_dict[sort_word] = [word]
    return list(anagram_dict.values())


arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(arr)
print(result)
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
