#problem statement:find the count of subarrays with xor k

class Solution:
    def subarrayXor(self, arr, k):
        h={}
        prefix=0
        h[prefix]=1
        count=0
        for n in arr:
            prefix=prefix^n
            if prefix^k in h:
                count+=h[prefix^k]
            if prefix not in h:
                h[prefix]=1
            else:
                h[prefix]+=1
        return count         
    
#pattern : prefix xor + hashmap  #time complexity : O(n)    