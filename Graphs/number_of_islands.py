# Problem: Count number of islands in grid (connected 1s)
# Pattern: DFS/BFS - Connected components in undirected graph
# Brute Force: DFS is inherently optimal, mark visited and count components
# Method: Iterate through grid, for each unvisited 1, do BFS/DFS and increment count
# Time: O(m*n), Space: O(m*n) for visited array

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        rows=len(grid)
        cols=len(grid[0])
        from collections import deque
        count=0
        visited=[[False]*cols for _ in range(rows)]
        
        def bfs(r, c):
            q=deque()
            q.append((r,c))
            visited[r][c]=True
            while q:
                row,col=q.popleft()
                for a,b in directions:
                    new_r=row+a
                    new_c=col+b
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c]=='1' and not visited[new_r][new_c]:
                        visited[new_r][new_c]=True
                        q.append((new_r,new_c))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1' and not visited[i][j]:
                    bfs(i,j)
                    count+=1
        return count