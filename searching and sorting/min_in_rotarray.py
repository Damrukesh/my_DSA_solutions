# Problem: Find minimum element in rotated sorted array
# Pattern: Binary Search on Rotated Array - Find where rotation point is
# Brute Force: Linear scan - O(n)
# Method: Check if left half is sorted, minimum is either l or in rotation half
# Time: O(log n), Space: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        ans=float('inf')
        while l<=r:
            mid=(l+r)//2
            if nums[l]<=nums[mid]:
                ans=min(ans,nums[l])
                l=mid+1
            else:
                ans=min(ans,nums[mid])
                r=mid-1
        return ans