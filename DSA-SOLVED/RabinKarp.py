"""
Rabin-Karp Algorithm for Pattern Searching

Problem: Given a text and a pattern, find all occurrences of the pattern in text.

Examples:
Input:  text = "THIS IS A TEST TEXT", pattern = "TEST"
Output: Pattern found at index 10

Input:  text = "AABAACAADAABAABA", pattern = "AABA"
Output: Pattern found at indices 0, 9, 12

Algorithm:
Rabin-Karp uses rolling hash to efficiently search for patterns:
1. Calculate hash value of pattern
2. Calculate hash value of first window in text
3. Slide the window one character at a time:
   - If hash values match, verify character by character
   - Recalculate hash for next window using rolling hash formula
4. Rolling hash allows O(1) hash recalculation instead of O(M)

Time Complexity: O(N+M) average case, O(N*M) worst case
Space Complexity: O(1)

Key Advantage: Can search for multiple patterns simultaneously
"""


def naive_pattern_search(text, pattern):
    """
    Naive pattern matching using substring comparison.

    Time Complexity: O(N*M) where N = len(text), M = len(pattern)
    Space Complexity: O(1)

    Note: This is a simple approach, not optimal for large texts.

    Args:
        text: The text to search in
        pattern: The pattern to search for

    Returns:
        Index of first occurrence, or -1 if not found
    """
    if not pattern or not text:
        return -1
    if pattern == text:
        return 0

    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            return i

    return -1


def rabin_karp_search(text, pattern, prime=101):
    """
    Rabin-Karp pattern searching using rolling hash.

    Time Complexity: O(N+M) average, O(N*M) worst case
    Space Complexity: O(1)

    Algorithm:
    1. Compute hash of pattern and first window of text
    2. For each window position:
       - If hashes match, verify with character comparison
       - Roll the hash to next window using formula:
         new_hash = (old_hash - first_char) * base + next_char

    Args:
        text: The text to search in
        pattern: The pattern to search for
        prime: Prime number for hash calculation (reduces collisions)

    Returns:
        List of starting indices where pattern is found
    """
    if not pattern or not text:
        return []

    n = len(text)
    m = len(pattern)

    if m > n:
        return []

    BASE = 256  # Number of characters in alphabet (extended ASCII)
    pattern_hash = 0
    text_hash = 0
    h = 1  # BASE^(m-1) % prime
    matches = []

    # Calculate h = BASE^(m-1) % prime
    # This is used for removing leading digit in rolling hash
    for i in range(m - 1):
        h = (h * BASE) % prime

    # Calculate initial hash values for pattern and first window of text
    for i in range(m):
        pattern_hash = (BASE * pattern_hash + ord(pattern[i])) % prime
        text_hash = (BASE * text_hash + ord(text[i])) % prime

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # If hash values match, verify character by character
        if pattern_hash == text_hash:
            # Check for characters one by one
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break

            if match:
                matches.append(i)
                print(f"Pattern found at index {i}")

        # Calculate hash for next window
        # Remove leading character and add trailing character
        if i < n - m:
            text_hash = (BASE * (text_hash - ord(text[i]) * h) +
                        ord(text[i + m])) % prime

            # Handle negative hash values
            if text_hash < 0:
                text_hash += prime

    return matches


# Test cases
if __name__ == "__main__":
    # Test 1: Naive approach
    text1 = "THIS IS A TEST TEXT"
    pattern1 = "TEST"
    print("Test 1 - Naive Pattern Search:")
    print(f"Text: '{text1}'")
    print(f"Pattern: '{pattern1}'")
    index = naive_pattern_search(text1, pattern1)
    print(f"First occurrence at index: {index}\n")



    # Test 2: Rabin-Karp
    text2 = "GEEKS FOR GEEKS"
    pattern2 = "GEEK"
    print("Test 2 - Rabin-Karp Search:")
    print(f"Text: '{text2}'")
    print(f"Pattern: '{pattern2}'")
    rabin_karp_search(text2, pattern2, prime=101)

    # Test 3: Multiple occurrences
    print("\nTest 3 - Multiple Occurrences:")
    text3 = "AABAACAADAABAABA"
    pattern3 = "AABA"
    print(f"Text: '{text3}'")
    print(f"Pattern: '{pattern3}'")
    rabin_karp_search(text3, pattern3, prime=101)
