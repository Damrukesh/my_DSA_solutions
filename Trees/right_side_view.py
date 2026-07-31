# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Problem: Right side view of a binary tree
# Pattern: Level-order traversal (BFS)
# Brute Force: Collect all nodes then filter by depth after traversal
# Method: BFS by level, append last node of each level
# Time: O(N), Space: O(N)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        from collections import deque
        q=deque()
        q.append(root)
        ans=[]
        while q:
            ans.append(q[-1].val)
            for _ in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans 
