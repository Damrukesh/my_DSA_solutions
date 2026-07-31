# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def hunt(root,p,q):
            if p.val > q.val:
                p, q = q, p
            if p.val<=root.val and q.val>=root.val:
                return root
            elif p.val<root.val and q.val<root.val:
                return hunt(root.left,p,q)
            else:
                return hunt(root.right,p,q)
        return hunt(root,p,q)