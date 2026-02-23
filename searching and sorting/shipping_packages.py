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

# trick is to calculate the number of days needed to ship all packages at the current guess of capacity (c) by iterating through the weights and accumulating them until they exceed c, at which point we increment the day count and reset the accumulated weight. If the total days needed is less than or equal to the given days, we try to find a smaller capacity, otherwise we try a larger capacity.                