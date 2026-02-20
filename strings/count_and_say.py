class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        count=1
        s=self.countAndSay(n-1)
        a=""
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                a=a+str(count)+s[i-1]
                count=1
        a=a+str(count)+s[-1]
        return a

# time complexity: O(n*2^n) 
# pattern: recursion, string manipulation



        

        