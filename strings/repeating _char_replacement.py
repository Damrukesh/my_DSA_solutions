# Problem: Longest substring with same character after replacing k characters
# Pattern: Hash Map + Sliding Window - Track max frequency in window
# Brute Force: Try all substrings and check if valid - O(n^2)
# Method: Maintain frequency map, shrink when (window_size - max_freq) > k
# Time: O(n), Space: O(1) fixed alphabet

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        maxi=0
        ans=0
        count={}
        for j in range(len(s)):
            count[s[j]]=count.get(s[j],0)+1
            maxi=max(maxi, count[s[j]])

            if (j-i+1)-maxi<=k:
                ans=max(ans,j-i+1)
            else:
                count[s[i]]-=1
                i+=1
        return ans