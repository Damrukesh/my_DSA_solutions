# problem: find if the given graph is a valid tree
# brute force solution: check if the graph is connected and has no cycles
# method: use dfs to check for cycles and connectivity
# time complexity: O(n)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        adj={i:[] for i in range(n)}
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        visited=set()
        prev=-1
        def dfs(root,prev):
            if root in visited:
                return False
            visited.add(root)
            for n in adj[root]:
                if n==prev:
                    continue
                if not dfs(n,root):
                    return False
            return True
        if not dfs(0,prev):
            return False
        return len(visited)==n


        