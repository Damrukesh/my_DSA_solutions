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
# Time: O(N) where N is the length of the input strings s and t. We have a single pass through both strings to check for isomorphism, which takes O(N) time.
# Space: O(1) if we don't consider the space used to store the input strings
# pattern: Hash Map, String Manipulation    