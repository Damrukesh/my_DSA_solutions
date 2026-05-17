# Problem: Find minimum coins needed to make amount, or -1 if impossible
# Pattern: Dynamic Programming - Unbounded Knapsack variant
# Brute Force: Recursion with backtracking - try each coin at each amount O(n^amount)
# Method: dp[i] = min coins for amount i, iterate through amounts and coins
# Time: O(amount * num_coins), Space: O(amount)

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