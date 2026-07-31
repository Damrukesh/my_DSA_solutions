# Problem: Check if two strings are anagrams
# Pattern: Hash Map - Count character frequencies
# Brute Force: Sort both strings and compare - O(n log n)
# Method: Count characters in first string, decrement with second string
# Time: O(n), Space: O(1) fixed alphabet

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h={}
        for a in s:
            if a in h:
                h[a]+=1
            else:
                h[a]=1
        for b in t:
            if b in h:
                h[b]-=1
            else:
                return False
        for c in h:
            if h[c]!=0:
                return False
        return True                 

        