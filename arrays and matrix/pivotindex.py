class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum=0
        for n in nums:
            sum+=n
        ns=0
        for i in range(len(nums)):
            if ns==sum-ns-nums[i]:
                return i
            ns+=nums[i]
        return -1        
#pattern : prefix sum  #time complexity : O(n)