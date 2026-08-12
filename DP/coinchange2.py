#problem:find the number of ways to make up a certain amount using given denominations of coins. Each coin can be used an unlimited number of times.
#brute force: check all combinations of coins to make up the amount - O(2^n)
#implemented approach: create 2d dp array where dp[i][j] represents the number of ways to make up amount j using the first i coins. Iterate through the coins and amounts, updating the dp array based on whether to include the current coin or not.
# time complexity: O(m*n), space complexity: O(m*n) where m is the number of coins and n is the amount.
#scope of improvement: can be optimized to use a 1d dp array instead of 2d, reducing space complexity to O(n) by iterating through the coins and updating the dp array in reverse order.


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m=len(coins)#rows
        n=amount+1 #cols
        dp=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j==0:
                    dp[i][j]=1
                    continue
                if j-coins[i]<0:
                    dp[i][j]=dp[i-1][j] if i>0 else 0
                else:
                    if i==0:
                        dp[i][j]=dp[i][j-coins[i]]
                        continue
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]
        return dp[m-1][n-1]
