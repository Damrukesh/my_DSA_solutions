# Problem: Find maximum sum of any contiguous subarray
# Pattern: Kadane's Algorithm - Dynamic Programming
# Brute Force: Check all subarrays and calculate their sums - O(n^2)
# Method: Track current sum and max sum, reset when current becomes negative
# Time: O(n), Space: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        sub=0
        for n in nums:
            if sub+n<0:
                sub=max(n,sub+n)
                ans=max(sub,ans)
                sub=0
            else:
                sub+=n
                ans=max(sub,ans)
        return ans