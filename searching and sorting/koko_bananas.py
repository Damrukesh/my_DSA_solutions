# Problem: Minimum eating speed to finish all piles within h hours
# Pattern: Binary Search on Answer - Check feasibility for each guess speed
# Brute Force: Try each speed from 1 to max(piles) - O(n * max_pile)
# Method: Binary search on speed, calculate hours needed for current guess
# Time: O(n log(max_pile)), Space: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        a=1
        b=max(piles)
        k=b
        while a<=b:
            c=(a+b)//2
            hours=0
            for d in piles:
                hours+=d//c
                if d%c!=0:
                    hours+=1
            if hours<=h:
                k=min(k,c)
                b=c-1
            else:
                a=c+1    
            c+=1
        return k