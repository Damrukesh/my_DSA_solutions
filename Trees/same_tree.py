# trick: Use DFS to traverse both trees simultaneously and compare their structure and values.
# time complexity: O(n) where n is the number of nodes in the trees. Each node is visited once.

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.flag=1
        def doubledfs(p,q):
            if not p and not q:
                return
            if p and q and p.val==q.val: 
                doubledfs(p.left,q.left)
                doubledfs(p.right,q.right)
            else:
                self.flag=0
        doubledfs(p,q)
        if self.flag==0:
            return False
        else:
            return True
        
# alternative solution using a more concise approach without using a flag variable:
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)
        
        