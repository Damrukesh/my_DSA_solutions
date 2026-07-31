# Problem: Find the length of the longest strictly increasing subsequence in an array.
# Brute force: Check all subsequences and verify increasing order, which is exponential.
# Solution approach: Use dynamic programming with dp[i] as the LIS starting at index i.
# Time complexity: O(n^2), Space complexity: O(n).class Solution:
def lengthOfLIS(self, nums: List[int]) -> int:
    n=len(nums)
    dp=[1]*n
    for i in range(len(nums)-2, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
        n-=1
    return max(dp)
    