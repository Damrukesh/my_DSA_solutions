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
# Time Complexity: O(N) where N is the number of nodes in the linked list
# Space Complexity: O(1) - only using a few pointers
# Pattern: Iterative Reversal with Three Pointers
# Trick: Use three pointers (prev, cur, next) to reverse the specified portion of the list in place by changing the direction of next pointers. Handle edge cases where left is 1 (reversing from head) and when right is the last node.
    