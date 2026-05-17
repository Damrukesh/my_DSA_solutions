# Problem: Find longest palindromic substring
# Pattern: Expand Around Center - Check each possible center
# Brute Force: Check all substrings - O(n^3)
# Method: For each character and pair, expand around center until mismatch
# Time: O(n^2), Space: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        anso=""
        anse=""
        #odd centre
        for i in range(len(s)):
            a,b=i,i+1
            while a>=0 and b<len(s):
                if s[a]==s[b]:
                    if (b-a+1)>len(anso):
                        anso=s[a:b+1]
                    a-=1
                    b+=1
                else:
                    break
        for i in range(len(s)):
            c,d=i,i
            while c>=0 and d<len(s):
                if s[c]==s[d]:
                    if (d-c+1)>len(anse):
                        anse=s[c:d+1]
                    c-=1
                    d+=1
                else:
                    break

        if len(anso)>len(anse):
            return anso
        else:
            return anse

            