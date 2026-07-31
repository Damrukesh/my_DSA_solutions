# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem: Count good nodes in a binary tree
# Pattern: DFS with path-maximum tracking
# Brute Force: Evaluate each root-to-node path separately
# Method: Recursive traversal that passes current max value
# Time: O(N), Space: O(H)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        m=root.val
        self.count=0
        def dfs(root,m):
            if not root:
                return 
            m=max(m,root.val)
            if root.val>=m:
                self.count+=1
            dfs(root.left, m)
            dfs(root.right, m)
            return
        dfs(root,m)
        return self.count
            

        