# Problem: Flood fill - change connected pixels of same color to new color
# Pattern: BFS (or DFS) - Graph traversal to visit all connected cells
# Brute Force: Recursion without queue could cause stack overflow for large areas
# Method: Use BFS with deque, mark visited by changing color, process neighbors
# Time: O(m*n), Space: O(m*n) for queue in worst case

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        R=len(image)
        C=len(image[0])
        from collections import deque
        q=deque()
        q.append((sr,sc))
        start=image[sr][sc]
        image[sr][sc]=color
        if start==color:
            return image
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                image[r][c]=color
                for a,b in directions:
                    row=a+r
                    col=b+c
                    if row in range(R) and col in range(C) and image[row][col]==start:
                        q.append((row,col))
                        image[row][col]=color
        return image