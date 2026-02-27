class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        a=1
        b=max(bloomDay)
        ans=b
        while a<=b:
            c=(a+b)//2
            bo=0
            fl=0
            for d in bloomDay:
                if d<=c:
                    fl+=1
                    if fl==k:
                        bo+=1
                        fl=0
                else:
                    fl=0    
            if bo>=m:
                ans=min(ans,c)
                b=c-1
            else:
                a=c+1

        if m * k > len(bloomDay):
            return -1
        else:    
            return ans                  
# pattern: binary search on answer, check if the current guess is valid by counting how many bouquets can be made with the given bloom day. If it's valid, try to find a smaller bloom day, otherwise try a larger bloom day.
