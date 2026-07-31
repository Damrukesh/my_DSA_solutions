# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem: Diameter of binary tree (longest path between nodes)
# Pattern: Tree DFS with height propagation
# Brute Force: Compute distances for all node pairs O(N^2)
# Method: DFS returns subtree height and updates max diameter
# Time: O(N), Space: O(H)

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

        
            
            

