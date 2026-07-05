# trick: BFS
# method: use a queue to traverse the tree level by level, incrementing depth at each level until all nodes are processed.

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



        