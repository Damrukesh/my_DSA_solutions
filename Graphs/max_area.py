"""
# Problem: Max area of island in a binary grid
# Pattern: Flood fill / DFS on grid
# Brute Force: For each cell, BFS/DFS without visited tracking repeats work
# Method: DFS with visited set to compute connected component size
# Time: O(R*C), Space: O(R*C)
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        R = len(grid)
        C = len(grid[0])
        visited = set()
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        def dfs(r, c):
            if (r, c) in visited or r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        max_area = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, dfs(i, j))
        return max_area


