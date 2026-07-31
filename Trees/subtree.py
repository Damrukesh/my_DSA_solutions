# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem: Check if one tree is a subtree of another
# Pattern: Tree comparison with DFS
# Brute Force: Compare each node against subtree via repeated traversal
# Method: Recursively match subtree at each node
# Time: O(N*M), Space: O(H)

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p,q):
            if not p and not q:
                return True
            if p and q and p.val==q.val:
                return same(p.left,q.left) and same(p.right,q.right)
            else:
                return False
        if root is None:
            return False

        if same(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)