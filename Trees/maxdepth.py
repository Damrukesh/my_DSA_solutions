# Problem: Maximum depth of a binary tree
# Pattern: BFS level count
# Brute Force: DFS tracking depth on each path manually
# Method: BFS by levels to count tree height
# Time: O(N), Space: O(N)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        from collections import deque
        q=deque()
        q.append(root)
        depth=0
        while q:
            l=len(q)
            for _ in range(l):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth+=1        
        return depth



        