# Problem: Remove Stars from String
# Time: O(n), Space: O(n)
# brute force: Use a list to store characters, pop when '*' is encountered, and join the list at the end.
# trick: Use a stack to keep track of characters, pop the last character when '*' is encountered, and finally join the stack to form the result string.

class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for c in s:
            if c=="*":
                stack.pop()
            else:
                stack.append(c)
        ans=""
        for c in stack:
            ans+=c
        return ans
