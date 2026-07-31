class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if not root:
                return
            temp=root.left
            root.left=root.right
            root.right=temp
            invert(root.left)
            invert(root.right)
        invert(root)
        return root
        