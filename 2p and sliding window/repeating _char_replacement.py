# Problem: Longest substring with same character after replacing k characters
# Pattern: Hash Map + Sliding Window - Track max frequency in window
# Brute Force: Try all substrings and check if valid - O(n^2)
# Method: Maintain frequency map, shrink when (window_size - max_freq) > k
# Time: O(n), Space: O(1) fixed alphabet

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        i,j=0,0
        ans=0
        while j<len(s):
            count[s[j]]=1+count.get(s[j],0)
            if (j-i+1)-max(count.values())<=k:
                ans=max(ans,j-i+1)
                j+=1
            else:
                count[s[i]]-=1
                i+=1
                j+=1
        return ans 