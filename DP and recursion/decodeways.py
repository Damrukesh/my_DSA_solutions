#trick: dp[i] = dp[i+1] + dp[i+2] if s[i:i+2] <= 26 else dp[i+1]
# time: O(n), space: O(n)
# brute force: recursion with memoization, time: O(n), space: O(n)

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
            