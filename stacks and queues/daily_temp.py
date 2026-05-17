# Problem: Find days until warmer temperature for each day
# Pattern: Monotonic Stack - Store indices, pop when finding larger element
# Brute Force: For each day, scan forward to find next warmer - O(n^2)
# Method: Use stack of indices, when current > top element, pop and record distance
# Time: O(n), Space: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nums=temperatures
        answer=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and nums[i]>stack[-1][0]:
                answer[stack[-1][1]]=i-stack[-1][1]
                stack.pop()
            stack.append([nums[i],i])    
        return answer