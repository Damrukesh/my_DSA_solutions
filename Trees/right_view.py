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
        
# time complexity is O(n) where n is the number of nodes in the tree
# space complexity is O(n) in the worst case when the tree is a complete binary tree
# traverse the tree level by level using bfs and store the value of the last node of each level in a list to get the right view of the tree.