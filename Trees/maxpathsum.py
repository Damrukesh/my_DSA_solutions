# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem: Maximum path sum in a binary tree
# Pattern: DFS with max path propagation
# Brute Force: Evaluate all paths explicitly
# Method: Recursively compute max single-branch sum and update global max
# Time: O(N), Space: O(H)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=float('-inf')
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            temp=max(root.val,root.val+left,root.val+right)
            self.ans=max(self.ans,temp,root.val+left+right)
            return temp
        dfs(root)
        return self.ans
            
        