# Problem: Find index of peak element (greater than neighbors)
# Pattern: Binary Search - Compare middle with neighbors to determine direction
# Brute Force: Linear scan - O(n)
# Method: Use binary search, compare mid with neighbors to find peak direction
# Time: O(log n), Space: O(1)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if mid>0 and nums[mid]<nums[mid-1]:
                r=mid-1
            elif mid<len(nums)-1 and nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                return mid    