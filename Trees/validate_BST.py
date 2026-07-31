# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem: Validate a binary tree is a binary search tree
# Pattern: DFS with min/max bounds
# Brute Force: Inorder traversal + sort/check values
# Method: Recursively enforce value ranges on subtrees
# Time: O(N), Space: O(H)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left=float('-inf')
        right=float('inf')
        def dfs(root,left,right):
            if not root:
                return True
            if not(root.val>left and root.val<right):
                return False
            return dfs(root.left,left,root.val) and dfs(root.right,root.val,right)
        return dfs(root,left,right)
