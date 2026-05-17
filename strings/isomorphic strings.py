# Problem: Check if two strings are isomorphic (character mapping is bijection)
# Pattern: Two Hash Maps - Track mapping in both directions
# Brute Force: Compare all permutations - O(n!)
# Method: Use two maps to ensure one-to-one character mapping
# Time: O(n), Space: O(1) fixed alphabet size

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sh={}
        th={}
        for i in range(len(s)):
            a,b=s[i],t[i]
            if (a in sh and sh[a]!=b) or (b in th and th[b]!=a):
                return False
            sh[a]=b
            th[b]=a
        return True    