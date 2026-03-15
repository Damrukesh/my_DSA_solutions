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

# pattern: monotonic stack
# time complexity: O(n)
# space complexity: O(n)
# The idea is to use a stack to keep track of the indices of the temperatures. We iterate through the list of temperatures, and for each temperature, we check if it is greater than the temperature at the top of the stack. If it is, we pop the stack and calculate the number of days until a warmer temperature is found. We continue this process until we find a temperature that is not greater than the current temperature or until the stack is empty. Finally, we push the current temperature and its index onto the stack.