# Problem: Valid palindrome 2 - alphanumeric only, case insensitive, allow 1 delete
# Pattern: Two Pointers + Greedy - Skip at most one character
# Brute Force: Try deleting each character and check palindrome - O(n^2)
# Method: Use two pointers, on mismatch try skipping left or right character
# Time: O(n), Space: O(1)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        def pal(l,r,s):
            while l<=r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True         

        while i<=j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return pal(i+1,j,s) or pal(i,j-1,s)
        return True 
        