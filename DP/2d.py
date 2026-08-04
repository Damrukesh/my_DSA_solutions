#problem: find the number of unique paths from top left to bottom right in a m*n grid
#brute force solution: use dp to store the number of unique paths from each cell to the bottom right cell
#approach: use bottom up dp to fill the dp table
#time complexity: O(m*n)
#space complexity: O(m*n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i+1==m or j+1==n:
                    dp[i][j]=1
                    continue
                dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]    