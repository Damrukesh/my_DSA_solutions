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

#complexity: O(n) where n is the length of the string s. We traverse the string once, and each character is processed in constant time. The space complexity is also O(n) in the worst case, when the stack holds all characters of the string.
#pattern: stack, string manipulation, parsing                         


        