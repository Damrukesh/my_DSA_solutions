#problem: find the maximum profit from stock prices with cooldown period
#brute force solution: generate all possible buy/sell combinations and find the maximum profit
#approach: dynamic programming with top down recursion and memoization ( DFS )
#time and space complexity: O(n), where n is the length of the prices array

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        dp={}
        buy=True
        def dfs(i,buy):
            if i>=len(prices):
                return 0
            if (i,buy) in dp:
                return dp[(i,buy)]
            if buy:
                take=dfs(i+1,False)-prices[i]
                skip=dfs(i+1,True)
                dp[(i,buy)]=max(take,skip)
            else:
                sell=prices[i]+dfs(i+2,True)
                skip=dfs(i+1,False)
                dp[(i,buy)]=max(sell,skip)
            return dp[(i,buy)]
        dfs(i,buy)
        return dp[(0,buy)]
        