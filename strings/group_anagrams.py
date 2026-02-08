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
    
# Time: O(NK) where N is the number of strings and K is the maximum length of a string in strs. We iterate through each string and count the frequency of each character, which takes O(K) time. The overall time complexity is O(NK).
# Space: O(NK) in the worst case, where all strings are different and have the same frequency of characters. In this case, we would have N entries in the ans dictionary, and each entry would store a list of strings that are anagrams of each other. The space complexity is O(NK) because we are storing all the strings in the ans dictionary.         
# pattern: Hash Map, String Manipulation

                 
            