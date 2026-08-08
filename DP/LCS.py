#problem: find the length of longest common subsequence of two strings
# brute force solution: generate all subsequences of both strings and find the longest common subsequence
# approach: dynamic programming,
# time and space complexity: O(m*n), where m and n are the lengths of the two strings

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m,-1,-1):
            for j in range(n,-1,-1):
                if i==m or j==n:
                    dp[i][j]=0
                    continue
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]
        
        