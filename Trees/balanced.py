# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.flag=1
        def dfs(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            left=1+dfs(root.left)
            right=1+dfs(root.right)
            if abs(left-right)>1:
                self.flag=0
            return max(left,right)
        dfs(root)
        if self.flag==0:
            return False
        else:
            return True
        