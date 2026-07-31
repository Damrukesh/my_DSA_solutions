# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem: Find k-th smallest element in BST
# Pattern: Inorder traversal of BST
# Brute Force: Collect all values and sort them
# Method: Traverse in-order and count until k
# Time: O(N), Space: O(H)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #self.ans=[]
        self.count=0
        self.ans=0
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.count+=1
            if self.count==k:
                self.ans=root.val
            inorder(root.right)
            return
        inorder(root)
        return self.ans
            
        
        