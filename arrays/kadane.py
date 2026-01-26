# https://leetcode.com/problems/maximum-subarray/description/
# maxium subarray sum using kadane's algorithm 


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