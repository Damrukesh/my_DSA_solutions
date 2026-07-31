# Problem: Find the maximum product of any contiguous subarray.
# Brute force: Evaluate every subarray product, which is O(n^2) or worse due to repeated multiplication.
# Solution approach: Track both maximum and minimum products ending at each position because negatives can flip sign.
# Time complexity: O(n), Space complexity: O(1).class Solution:
def maxProduct(self, nums: List[int]) -> int:
    m1,m2=1,1
    ans=float("-inf")
    for i in range(len(nums)-1,-1,-1):
        a,b=m1,m2
        m1=max(nums[i],nums[i]*a,nums[i]*b)
        m2=min(nums[i],nums[i]*a,nums[i]*b)
        ans=max(ans,m1)
    return ans
    
    