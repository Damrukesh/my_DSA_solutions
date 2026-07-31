class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS=len(grid)
        COLS=len(grid[0])
        from collections import deque
        q=deque()
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    q.append((i,j))
        while q:
            a,b=q.popleft()
            for i,j in directions:
                val=grid[a][b]
                row=a+i
                col=b+j
                if row in range(ROWS) and col in range(COLS) and grid[row][col]!=-1 and grid[row][col]!=0 and grid[row][col]==2147483647:
                    grid[row][col]=val+1
                    q.append((row,col))

        