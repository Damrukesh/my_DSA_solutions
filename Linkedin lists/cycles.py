
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        s=set()
        while cur:
            if cur in s:
                return cur
            s.add(cur)
            cur=cur.next
             
# Time Complexity: O(N) where N is the number of nodes
# Space Complexity: O(N) for storing nodes in the set
# Pattern: Hash Set Detection
# Alternative Pattern (Floyd's Cycle Detection): Two Pointers - use slow moving 1 step and fast moving 2 steps
# Trick: If there's a cycle, slow and fast pointers will meet. Then find cycle start by moving one pointer to head and moving both 1 step at a time
        