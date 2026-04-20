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
# pattern: monotonic stack
# time complexity: O(n)
# space complexity: O(n)
# The idea is to use a stack to keep track of the indices of the elements in the input list. We iterate through the list twice (using modulo to wrap around) and for each element, we check if it is greater than the element at the top of the stack. If it is, we pop the stack and update the answer for that index with the current element. We continue this process until we find an element that is not greater than the current element or until the stack is empty. Finally, we push the current index onto the stack if we are in the first pass through the list.    
    