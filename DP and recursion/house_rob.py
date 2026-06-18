# 198. House Robber 
# trick: dp[i] = max(dp[i-1], nums[i]+dp[i-2])
# Problem: Given an array of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police (you cannot rob adjacent houses).



class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        nums[1] = max(nums[0], nums[1])    
        for i in range(2,len(nums)):
            nums[i]=max(nums[i-1],nums[i]+nums[i-2])
        return nums[len(nums)-1]


        