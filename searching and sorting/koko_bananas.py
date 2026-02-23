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
        
# pattern: binary search on answer, check if the current guess is valid by calculating the hours needed to eat all piles at that speed. If it's valid, try to find a smaller speed, otherwise try a larger speed.
# trick is to calculate hours needed for each pile using integer division and adding 1 if there's a remainder, which is equivalent to math.ceil(d/c).