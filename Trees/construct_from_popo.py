# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem: Construct binary tree from preorder and inorder traversal
# Pattern: Divide and conquer using tree traversal properties
# Brute Force: Try all tree shapes matching traversals
# Method: Recursively build left/right subtrees from inorder split
# Time: O(N^2) worst-case due to index() on inorder, Space: O(N)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n=len(inorder)
        if not preorder or not inorder:
            return None
        root=TreeNode(preorder[0])
        pos=inorder.index(root.val)
        root.left=self.buildTree(preorder[1:pos+1],inorder[0:pos])
        root.right=self.buildTree(preorder[pos+1:len(preorder)],inorder[pos+1:len(inorder)])
        return root
        