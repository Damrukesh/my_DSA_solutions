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

# Time: O(N) where N is the length of the input string s. We have a single pass through the string to check for palindromicity, and in the worst case, we may need to check two additional substrings (one by skipping the left character and one by skipping the right character), which also takes O(N) time.
# Space: O(1) if we don't consider the space used to store the input string
# pattern: Two Pointers, Greedy 
        