def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        if s[right] in char_map:
            # Move left pointer to the right of the last seen index of the character
            # but only if it's within the current window
            left = max(left, char_map[s[right]] + 1)
        
        char_map[s[right]] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len

# Time Complexity: O(n)
# Space Complexity: O(min(n, m)) where m is the size of the alphabet