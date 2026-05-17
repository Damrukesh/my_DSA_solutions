# Problem: Detect if linked list has a cycle and return cycle start node
# Pattern: Hash Set Detection (or Floyd's Cycle Detection Algorithm)
# Brute Force: Hash Set - mark visited nodes and check if revisited - O(n) space
# Method: Use two pointers (slow 1 step, fast 2 steps). If they meet, cycle exists.
# Time: O(n), Space: O(1) with Floyd's algorithm

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        s=set()
        while cur:
            if cur in s:
                return cur
            s.add(cur)
            cur=cur.next
        