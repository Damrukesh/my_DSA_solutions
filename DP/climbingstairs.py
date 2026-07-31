# Problem: Count distinct ways to climb a staircase of n steps using 1 or 2 steps at a time.
# Brute force: Recursively explore all combinations of 1-step and 2-step moves, resulting in O(2^n) time.
# Solution approach: Use dynamic programming to compute the number of ways bottom-up with memoization.
# Time complexity: O(n), Space complexity: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[n]=1
        dp[n-1]=1
        while n>=2:
            dp[n-2]=dp[n-1]+dp[n]
            n-=1
        return dp[0]
