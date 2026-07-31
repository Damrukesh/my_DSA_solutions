# Problem: Find index where left sum equals right sum (pivot/equilibrium index)
# Pattern: Prefix Sum - Calculate total then match left sum with right sum
# Brute Force: For each index, calculate left and right sums - O(n^2)
# Method: First pass get total sum, second pass maintain running sum and compare
# Time: O(n), Space: O(1)

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