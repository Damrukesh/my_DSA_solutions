#problem statement: There are n cars going to the same destination along a one-lane road. The destination is target miles away.
#brute force: sort the cars by position and iterate from the back, if the time to reach the target is greater than the last time, it is a new fleet
#approach: sort the cars by position and iterate from the back, if the time to reach the target is greater than the last time, it is a new fleet
#time complexity: O(n log n) for sorting, O(n) for iterating through the cars, so overall O(n log n)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        fleet=0
        for i in range(len(position)):
            speed[i]=(target-position[i])/speed[i]
            cars.append((position[i],speed[i]))
        cars.sort()
        tl=0
        for i in range(len(position)-1,-1,-1):
            p,t=cars[i]
            if t>tl:
                fleet+=1
            tl = max(tl, t)
        return fleet

        
        