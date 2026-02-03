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

            
#problem statement:buy and sell stock once to maximize profit
#pattern : track min price and max profit #time complexity : O(n)