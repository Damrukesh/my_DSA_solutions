# trick: inorder traversal of BST gives sorted order
# time: O(n), space: O(n)
# brute force: add to list and sort, time: O(nlogn), space: O(n)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.ans.append(root.val)
            inorder(root.right)
            return
        inorder(root)
        return self.ans[k-1]
            
        
        