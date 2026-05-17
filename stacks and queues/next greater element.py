# Problem: Find next greater element for each element (circular array)
# Pattern: Monotonic Stack - Iterate twice to handle circular array
# Brute Force: For each element, scan forward to find greater - O(n^2)
# Method: Use stack of indices, iterate through array twice (modulo n)
# Time: O(n), Space: O(n)

class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1] * n
        stack = []  # stores indices

        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                idx = stack.pop()
                ans[idx] = nums[i % n]

            if i < n:
                stack.append(i)

        return ans    
    