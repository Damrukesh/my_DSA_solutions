# Problem: Minimum bloom day needed to make m bouquets with k consecutive flowers each
# Pattern: Binary Search on Answer - Check feasibility for each guess
# Brute Force: Try each day sequentially - O(max_day * n)
# Method: Binary search on bloom day, count valid bouquets for that day
# Time: O(n log(max_day)), Space: O(1)

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
