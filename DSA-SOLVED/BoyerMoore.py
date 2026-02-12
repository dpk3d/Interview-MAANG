"""
Boyer-Moore String Matching Algorithm

Problem: Pattern searching in text.
Given a text txt[0..n-1] and a pattern pat[0..m-1] where n is the length of
the text and m is the length of the pattern, find all occurrences of pat[] in txt[].

Examples:
Input:  txt = "THIS IS A TEST TEXT", pat = "TEST"
Output: Pattern found at index 10

Input:  txt = "AABAACAADAABAABA", pat = "AABA"
Output: Pattern found at index 0, 9, 12

Algorithm:
Boyer-Moore is an efficient string searching algorithm that skips characters
intelligently using two heuristics:
1. Bad Character Heuristic (implemented here)
2. Good Suffix Heuristic (not implemented in this version)

Time Complexity: O(N/M) best case, O(N*M) worst case
Space Complexity: O(1) - constant space for character set
"""

NO_OF_CHARS = 256  # Extended ASCII character set


def build_bad_char_table(pattern):
    """
    Preprocessing function for Boyer Moore's bad character heuristic.

    Creates a table that stores the rightmost occurrence of each character
    in the pattern. This helps determine how far to shift the pattern when
    a mismatch occurs.

    Args:
        pattern: The pattern string to search for

    Returns:
        List of size NO_OF_CHARS where index represents ASCII value and
        value represents the rightmost position of that character in pattern
        (-1 if character doesn't exist in pattern)
    """
    # Initialize all occurrences as -1
    bad_char = [-1] * NO_OF_CHARS

    # Fill the actual value of last occurrence of each character
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i

    return bad_char


def boyer_moore_search(text, pattern):
    """
    Pattern searching function using Bad Character Heuristic of Boyer Moore.

    Algorithm:
    1. Align pattern with beginning of text
    2. Compare pattern from right to left
    3. On mismatch, shift pattern based on bad character heuristic:
       - If mismatched character exists in pattern, align it
       - Otherwise, shift pattern past the mismatched character
    4. Repeat until pattern moves past the text

    Args:
        text: The text string to search in
        pattern: The pattern string to search for

    Returns:
        List of starting indices where pattern is found
    """
    m = len(pattern)
    n = len(text)

    if m == 0 or n == 0 or m > n:
        return []

    # Build bad character table for the pattern
    bad_char = build_bad_char_table(pattern)

    matches = []
    shift = 0  # Shift of the pattern with respect to text

    while shift <= n - m:
        j = m - 1

        # Keep reducing index j while characters match
        # Compare from right to left
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        # If pattern is found at current shift
        if j < 0:
            matches.append(shift)
            print(f"Pattern found at index {shift}")

            # Shift pattern to align next character in text with its
            # last occurrence in pattern
            if shift + m < n:
                shift += m - bad_char[ord(text[shift + m])]
            else:
                shift += 1
        else:
            # Shift pattern to align bad character in text with its
            # last occurrence in pattern
            # Use max to ensure positive shift
            shift += max(1, j - bad_char[ord(text[shift + j])])

    return matches


# Test cases
if __name__ == "__main__":
    # Test 1
    text1 = "ABAAABCD"
    pattern1 = "ABC"
    print(f"Searching for '{pattern1}' in '{text1}':")
    boyer_moore_search(text1, pattern1)

    # Test 2
    print(f"\nSearching for 'AABA' in 'AABAACAADAABAABA':")
    text2 = "AABAACAADAABAABA"
    pattern2 = "AABA"
    boyer_moore_search(text2, pattern2)

    # Test 3
    print(f"\nSearching for 'TEST' in 'THIS IS A TEST TEXT':")
    text3 = "THIS IS A TEST TEXT"
    pattern3 = "TEST"
    boyer_moore_search(text3, pattern3)
