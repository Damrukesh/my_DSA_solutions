# trick: Use DFS to traverse the main tree and check for subtree matches using the same tree comparison function.
# time complexity: O(m*n) where m is the number of nodes in the main tree and n is the number of nodes in the subtree. In the worst case, we may have to compare each node of the main tree with the subtree.
# brute force approach: For each node in the main tree, check if the subtree rooted at that node is the same as the given subtree using the same tree comparison function.


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