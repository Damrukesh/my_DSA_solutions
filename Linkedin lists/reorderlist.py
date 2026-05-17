# Problem: Reorder list as L0->Ln->L1->Ln-1->... (interleave first and last halves reversed)
# Pattern: Slow/Fast Pointers + List Reversal + Merge - Find mid, reverse second half, merge
# Brute Force: Store nodes in array, reorder in place - O(n) space
# Method: Find middle, reverse second half, alternately pick from both halves
# Time: O(n), Space: O(1) in-place

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        a=slow.next
        slow.next=None
        prev=None      
        while a:
            cur=a
            a=cur.next
            cur.next=prev
            prev=cur
        start=head
        end=prev
        while end:
            temp2=start.next
            start.next=end
            start=temp2
            temp1=end.next
            end.next=start
            end=temp1