class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        count=1
        cur=head
        while cur.next:
            cur=cur.next
            count+=1
        new=head
        s=count-(k%count)-1
        if not k%count:
            return head    
        while s:
            new=new.next
            s-=1
        start=new.next
        new.next=None
        cur.next=head
        return start

# Time Complexity: O(N) where N is the number of nodes
# Space Complexity: O(1) - only using a few pointers
# Pattern: Two Pointers with Length Calculation
# Trick: Find list length, calculate rotation point, break the list there, and reconnect to form rotated list. Optimize with modulo (k % count) to handle rotations > length