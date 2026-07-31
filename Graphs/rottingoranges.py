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
            
        