# tree diameter is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# trick is to find the longest path from left and right subtrees and add them together. The longest path from left and right subtrees can be found by finding the height of the left and right subtrees. The height of a tree is the number of edges on the longest path from the root to a leaf node.
# pattern: recursive tree traversal, postorder traversal, depth first search, height of a tree, longest path in a tree, binary tree diameter, tree diameter algorithm, tree diameter problem, tree diameter solution, tree diameter implementation


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
