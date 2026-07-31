# Problem: Maximize the amount of money robbed from houses arranged in a line without robbing adjacent houses.
# Brute force: Try all subsets of houses and check adjacency constraints, which is exponential.
# Solution approach: Use dynamic programming to maintain the maximum loot ending at each house.
# Time complexity: O(n), Space complexity: O(1) if modifying input, otherwise O(n).
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


        