class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        n=len(nums)
        dp=[0]*n
        dp[n-1]=0
        dp[n-2]=nums[n-2]
        while n>=3:
            dp[n-3]=max(nums[n-3]+dp[n-1],dp[n-2])
            n-=1
        ans1=dp[0]
        n=len(nums)
        dp.append(0)
        dp[n-1]=nums[n-1]
        while n>=3:
            dp[n-2]=max(nums[n-2]+dp[n],dp[n-1])
            n-=1
        return max(ans1,dp[1])
        