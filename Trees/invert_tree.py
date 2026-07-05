# Definition for a binary tree node.
# trick: recursively swap the left and right children of each node in the tree.


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        temp=root.right
        root.right=root.left
        root.left=temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
