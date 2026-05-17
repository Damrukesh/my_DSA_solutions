# Problem: Binary tree zigzag level order traversal (alternate direction per level)
# Pattern: BFS Level Order Traversal - Reverse alternate levels
# Brute Force: Store all values, sort by level, then reverse alternate levels
# Method: BFS queue process level by level, reverse every other level
# Time: O(n), Space: O(w) where w is max width

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