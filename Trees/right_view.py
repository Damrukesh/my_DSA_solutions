# Problem: Binary tree right side view (rightmost node at each level)
# Pattern: BFS Level Order Traversal - Take last node of each level
# Brute Force: DFS tracking depth, store rightmost at each depth - O(n)
# Method: BFS queue, process level by level, append last node value
# Time: O(n), Space: O(w) where w is max width

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        q=deque()
        q.append(root)
        res=[]
        while q:
            res.append(q[-1].val)
            for _ in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res