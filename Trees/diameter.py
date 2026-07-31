# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        self.result=0
        def hunt(root):
            if not root:
                return 0
            left=hunt(root.left)
            right=hunt(root.right)
            self.result=max(self.result,left+right)
            return 1+max(left,right)
        hunt(root)
        return self.result

        
            
            

