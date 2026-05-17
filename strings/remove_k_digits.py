# Problem: Remove k digits to form smallest possible number
# Pattern: Greedy + Monotonic Stack - Remove larger digits when possible
# Brute Force: Generate all combinations of removing k digits - O(C(n,k))
# Method: Use stack, pop larger digits while k>0, handle leading zeros
# Time: O(n), Space: O(n)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for c in num:
            while stack and stack[-1]>c and k>0:
                stack.pop()
                k-=1
            stack.append(c)
        if k>0:
            while k > 0:
                stack.pop()
                k -= 1
        l=0
        while l<len(stack) and stack[l]=='0':
            l+=1
        ans=""
        for d in range(l,len(stack)):
            ans+=stack[d]
        if ans=="":
            return '0'
        else:
            return ans