# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        ans=[]
        q=deque()
        q.append(root)
        while q:
            res=[]
            for _ in range(len(q)):
                a=q.popleft()
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
                res.append(a.val)
            ans.append(res)
        return ans 

        