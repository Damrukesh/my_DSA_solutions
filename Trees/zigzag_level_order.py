class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        q=deque([root])
        result=[]
        while q:
            res=[]
            for i in range(len(q)):
                res.append(q[i].val)
            result.append(res)    
            for _ in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        for i in range(1,len(result),2):
            result[i].reverse()            
        return result

# time complexity is O(n) where n is the number of nodes in the tree
# space complexity is O(n) in the worst case when the tree is a complete binary tree
# traverse the tree level by level using bfs and store the values of each level in a list, then reverse the values of every alternate level to get the zigzag order.