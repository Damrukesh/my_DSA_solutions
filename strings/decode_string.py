# Problem: Decode encoded string (k[encoded_string])
# Pattern: Stack + String Parsing - Handle nested brackets
# Brute Force: Recursion for each bracket level
# Method: Use stack to store characters, process closing bracket to expand pattern
# Time: O(max_k^n), Space: O(n) where max_k is largest multiplier

class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        num=""
        ans=""
        for c in s:
            if c==']':
                temp=""
                while stack and stack[-1]!='[':
                    temp=stack.pop()+temp
                stack.pop()
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                for i in range(int(num)):
                    stack.append(temp)
                temp=""
                num=""
            else:
                stack.append(c)
        for d in stack:
            ans+=d
        return ans                         


        