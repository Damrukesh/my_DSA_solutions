class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for i in range(len(dp)):
            for c in coins:
                if i-c>=0:
                    dp[i]=min(dp[i],1+dp[i-c])
        if dp[amount]==float('inf'):
            return -1
        else:
            return dp[amount]                
# trick: Use a dp array where dp[i] represents the minimum coins needed for amount i. Initialize with infinity and set dp[0]=0. For each amount, iterate through coins and update dp[i] with the minimum of current dp[i] and 1 + dp[i - coin]. Finally, check if dp[amount] is still infinity, return -1 if it is, otherwise return dp[amount].
# Time Complexity: O(amount * number of coins)
#pattern: Dynamic Programming - Unbounded Knapsack