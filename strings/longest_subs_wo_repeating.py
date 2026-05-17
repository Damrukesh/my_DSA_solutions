# Problem: Find length of longest substring without repeating characters
# Pattern: Hash Map + Sliding Window - Store last index of each character
# Brute Force: Check all substrings - O(n^2)
# Method: Use hash map for O(1) lookup, slide window avoiding repeats
# Time: O(n), Space: O(m) where m is charset size

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st={}
        i,j=0,0
        ans=0
        while j<len(s):
            if s[j] not in st:
                st[s[j]]=j
            else:
                i=max(i,st[s[j]]+1)
                st[s[j]]=j
            ans=max(ans,j-i+1)
            j+=1  
        return ans