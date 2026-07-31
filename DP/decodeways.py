# Problem: Count ways to decode a digit string where 'A'->1, 'B'->2, ..., 'Z'->26.
# Brute force: Try splitting the string at every possible point and validate each decode, leading to exponential time.
# Solution approach: Use dynamic programming from the end to count valid decodings for each suffix.
# Time complexity: O(n), Space complexity: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if n<=1 and int(s[0])>=1:
             return 1
        elif n<=1 and int(s[0])<1:
            return 0
        dp=[0]*(n+1)
        dp[n]=1
        if n>=2 and int(s[n-1])!=0:
            dp[n-1]=1
        else:
            dp[n-1]=0
        while n>=2:
            add=dp[n-1]
            if int(s[n-2]+s[n-1])<=26:
                add+=dp[n]
            if s[n-2]=='0':
                dp[n-2]=0
            else:
                dp[n-2]=add
            n-=1
        return dp[0]
            
                   
        