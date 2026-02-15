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

             
        


                                                                                           