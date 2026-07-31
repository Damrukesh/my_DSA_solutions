# problem statement: find the maximum area of water that can be contained by the heights of the walls given in the list heights. The width of the container is determined by the distance between the two walls, and the height is determined by the shorter wall.
# brute force: check all pairs of walls and calculate the area for each pair - O(n^2)
# implemented approach: two pointer technique - start with two pointers at the beginning and end of the list, calculate the area, and move the pointer pointing to the shorter wall towards the other pointer. Repeat until the pointers meet.
# time complexity: O(n), space complexity: O(1)


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        ans=float('-inf')
        while i<=j:
            area=(j-i)*min(heights[i],heights[j])
            ans=max(ans,area)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return ans        
