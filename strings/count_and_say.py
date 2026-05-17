# Problem: Count and say sequence (n-th number in sequence)
# Pattern: Recursion + String Manipulation - Count consecutive characters
# Brute Force: Not applicable - sequence inherently recursive
# Method: Get (n-1)th sequence, count consecutive chars, build string
# Time: O(n*2^n), Space: O(2^n) for recursion and output

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



        

        