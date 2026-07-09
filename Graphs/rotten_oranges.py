# Problem: Find minimum time for all oranges to rot (multi-source BFS)
# Pattern: Multi-level BFS - Process all rotten oranges level by level
# Brute Force: Simulate each day separately - O(m*n*days)
# Method: Start with all rotten oranges in queue, process layer by layer
# Time: O(m*n), Space: O(m*n) for queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        ROWS=len(grid)
        COLS=len(grid[0])
        direction=[(-1,0),(1,0),(0,1),(0,-1)]
        q=deque()
        fresh=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
        time=-1
        while q:
            for orange in range(len(q)):
                r,c=q.popleft()
                for i,j in direction:
                    row=r+i
                    col=c+j
                    if row in range(ROWS) and col in range(COLS) and grid[row][col]==1:
                        fresh-=1
                        grid[row][col]=2
                        q.append((row,col))
            time+=1
        if fresh==0:
            return time
        else:
            return -1
            
        