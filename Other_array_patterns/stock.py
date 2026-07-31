# Problem: Buy and sell stock once to maximize profit
# Pattern: Track minimum price seen so far and calculate profit at each point
# Brute Force: Check all pairs of buy/sell prices - O(n^2)
# Method: Single pass - maintain min price, calculate max profit at each price
# Time: O(n), Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        i,j=0,0
        min_price=float('inf')
        max_profit=0
        for i in range(len(prices)):
            max_profit=max(max_profit,prices[i]-min_price)
            min_price=min(prices[i],min_price)
        return max_profit