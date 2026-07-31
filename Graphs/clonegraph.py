"""
# Problem: Clone an undirected graph (deep copy)
# Pattern: Graph Traversal (DFS/BFS) with Hash Map to map originals to copies
# Brute Force: Recreate nodes without mapping leads to duplicate nodes for cycles
# Method: DFS/BFS and a dictionary mapping original node -> cloned node
# Time: O(V + E), Space: O(V)
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned={}
        def dfs(node):
            if not node:
                return None
            if node in cloned:
                return cloned[node]
            copy=Node(node.val)
            cloned[node]=copy
            for n in node.neighbors:
                copy.neighbors.append((dfs(n)))
            return copy
        return dfs(node)

        