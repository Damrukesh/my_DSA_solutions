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
# Time: O(N) where N is the length of the input strings s and t. We have a single pass through both strings to count the frequency of characters, which takes O(N) time.
# Space: O(1) if we don't consider the space used to store the input strings
# pattern: Hash Map, String Manipulation                 

        