# Problem: Find the minimum cost to climb stairs given a cost array, where you can take 1 or 2 steps.
# Brute force: Try all step combinations and sum costs, which is exponential.
# Solution approach: Use dynamic programming to accumulate minimum cost to reach each step.
# Time complexity: O(n), Space complexity: O(1) if modifying input, otherwise O(n).
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
  
        for i in range(2, N):
            cost[i] += min(cost[i - 1], cost[i - 2])

        return min(cost[N - 1], cost[N - 2])