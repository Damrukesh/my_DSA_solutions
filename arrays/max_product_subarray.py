#problem statement:find the maximum product subarray

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
    
#pattern : kadane's algorithm variation  #time complexity : O(n)