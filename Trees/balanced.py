# time complexity: O(n)
# trick: if the left and right subtree are balanced, then the current tree is balanced
# brute force: check the height of left and right subtree, if the difference is greater than 1, then return False
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.flag=1
        def dfs(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            left=1+dfs(root.left)
            right=1+dfs(root.right)
            if abs(left-right)>1:
                self.flag=0
            return max(left,right)
        dfs(root)
        if self.flag==0:
            return False
        else:
            return True
        