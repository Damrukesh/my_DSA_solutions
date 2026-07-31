class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        visited=[]
        rows=len(grid)
        columns=len(grid[0])
        islands=0
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visited.append((r,c))
            while q:
                rr,cc=q.popleft()
                for a,b in directions:
                    row=rr+a
                    col=cc+b
                    if row in range(rows) and col in range(columns) and grid[row][col]=='1' and (row,col) not in visited:
                        visited.append((row,col))
                        q.append((row,col))
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]=="1" and (i,j) not in visited:
                    bfs(i,j)
                    islands+=1
        return islands







        