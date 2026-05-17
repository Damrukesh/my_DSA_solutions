# Problem: Reverse nodes between positions left and right (1-indexed)
# Pattern: Iterative Reversal with Dummy Node + Three Pointers
# Brute Force: Reverse entire list, rotate to position, reverse back
# Method: Use dummy node, isolate segment to reverse, reverse it, reconnect to main list
# Time: O(n), Space: O(1) only pointer storage

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur=head
        count=1
        old=ListNode(0)
        dummy=old
        old.next=head
        for _ in range(left-1):
            old=old.next
        r=old.next 
        for _ in range(right-left+1):
            r=r.next   
        a=old.next
        b=old.next
        prev=None      
        for _ in range(right-left+1):  
            cur=a
            a=cur.next
            cur.next=prev
            prev=cur
        old.next=prev
        b.next=r
        return dummy.next
    