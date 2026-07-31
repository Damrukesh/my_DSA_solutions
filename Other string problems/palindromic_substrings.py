# Problem: Count number of palindromic substrings
# Pattern: Expand Around Center - Check each possible center
# Brute Force: Check all substrings - O(n^3)
# Method: For each character and pair, expand around center, count palindromes
# Time: O(n^2), Space: O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # Odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            # Even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count
