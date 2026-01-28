class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        s=0
        ans=float('inf')
        while r<len(nums) and l<=r:
            s+=nums[r]
            if s>=target:
                s-=nums[l]
                ans=min(ans,r-l+1)
                l+=1
                s-=nums[r]               
            else:
                r+=1
        if ans==float('inf'):
            return 0
        else:
            return ans    

            


        