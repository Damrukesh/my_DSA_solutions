# Problem: Find maximum in every sliding window of size k
# Pattern: Deque + Sliding Window - Store indices of useful elements
# Brute Force: For each window, scan all k elements - O(n*k)
# Method: Deque stores indices in decreasing order of values, remove old indices outside window
# Time: O(n), Space: O(k)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=collections.deque()
        ans=[]
        l,r=0,0

        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            if r-l+1==k:
                ans.append(nums[q[0]])
                l+=1
            if l>q[0]:
                q.popleft()
            r+=1
        return ans   