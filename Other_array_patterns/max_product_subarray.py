# Problem: Find maximum product of any contiguous subarray
# Pattern: Kadane's Algorithm variation - Track both max and min products
# Brute Force: Check all subarrays and calculate their products - O(n^2)
# Method: Track max and min product at each position (negative can flip to positive)
# Time: O(n), Space: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=1
        mini=1
        gb=nums[0]
        for n in nums:
            m=maxi
            maxi=max(n*maxi,n*mini,n)
            mini=min(n*m,n*mini,n)
            gb=max(gb,maxi)
        return gb