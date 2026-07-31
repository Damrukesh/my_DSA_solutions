# Problem: Find length of longest substring without repeating characters
# Pattern: Hash Map + Sliding Window - Store last index of each character
# Brute Force: Check all substrings - O(n^2)
# Method: Use hash map for O(1) lookup, slide window avoiding repeats
# Time: O(n), Space: O(m) where m is charset size

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0  
        h={}
        i,j=0,0
        ans=0
        while j<len(s):
            if s[j] in h:
                i=max(i,h[s[j]]+1)
            ans=max(ans,j-i+1)
            h[s[j]]=j
            j+=1
        return ans
#mistake : max(i,h[s[j]]+1)