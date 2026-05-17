# Problem: Rotate linked list right by k positions
# Pattern: Two Pointers with Length Calculation - Find rotation point
# Brute Force: Rotate one by one k times - O(n*k)
# Method: Find length, calculate new start position (length - k%length), reconnect
# Time: O(n), Space: O(1) only pointer storage

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