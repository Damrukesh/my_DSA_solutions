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

# Time Complexity: O(log N) where N is the number of elements
# Space Complexity: O(1)
# Pattern: Binary Search on Rotated Array
# Trick: Check if left half is sorted (nums[l] <= nums[mid]). If yes, minimum is in left half or current l. If no, minimum must be in the area containing the rotation point