class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #find rotten orange
        rows=len(grid)
        cols=len(grid[0])
        from collections import deque
        q=deque()
        timer,fresh=0,0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                for a,b in directions:
                    row=r+a
                    col=c+b
                    if row in range(rows) and col in range(cols) and grid[row][col]==1:
                        q.append((row,col))
                        fresh-=1
                        grid[row][col]=2
            timer+=1        
        if fresh>0:
            return -1
        else:
            return timer            

# time complexity is O(m*n) where m and n are the number of rows and columns in the grid
# space complexity is O(m*n) in the worst case when all oranges are rotten and we have to add all of them to the queue.
# traverse the grid once to find the rotten oranges and count the fresh oranges, then use bfs to rot the fresh oranges and count the time taken.