# Problem: Group strings that are anagrams together
# Pattern: Hash Map with Character Frequency as Key
# Brute Force: Compare each string with all others - O(n^2 * k log k)
# Method: Create frequency tuple for each string as key, group by key
# Time: O(n*k log k), Space: O(n*k) where n is strings, k is avg length

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        count=[0]*26
        for c in strs:
            for s in c:
                count[ord(s)-ord("a")]+=1
            if tuple(count) in ans:
                ans[tuple(count)].append(c)
            else:
                ans[tuple(count)]=[c]
            count=[0]*26  
        return list(list(ans.values()))

                 
            