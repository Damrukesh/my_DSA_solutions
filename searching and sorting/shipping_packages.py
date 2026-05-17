# Problem: Ship all packages within days with minimum capacity
# Pattern: Binary Search on Answer - Check feasibility for each guess capacity
# Brute Force: Try each capacity from max_weight to sum - O(n * sum)
# Method: Binary search on capacity, count days needed for current capacity
# Time: O(n log(sum)), Space: O(1)

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        a=max(weights)
        b=sum(weights)
        ans=b
        while a<=b:
            c=(a+b)//2
            weight=0
            da=0
            i=0
            for d in weights:
                if weight+d<=c:
                    weight+=d
                else:
                    weight=d
                    da+=1
            da+=1
            if da<=days:
                ans=min(c,ans)
                b=c-1
            else:
                a=c+1
        return ans                