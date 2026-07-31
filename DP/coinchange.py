# Problem: Given coin denominations and an amount, find the minimum number of coins needed to make that amount.
# Brute force: Try all combinations of coins for the target amount, which is exponential in amount and coin count.
# Solution approach: Use dynamic programming to build up the minimum coins for each sub-amount.
# Time complexity: O(amount * len(coins)), Space complexity: O(amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for a in range(amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a]=min(dp[a],1+dp[a-c])
        if dp[amount]==amount+1:
            return -1
        else:
            return dp[amount]
        