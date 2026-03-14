# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        a=slow
        prev=None      
        while a:
            cur=a
            a=cur.next
            cur.next=prev
            prev=cur   
        
        while prev:
            if head.val==prev.val:
                head=head.next
                prev=prev.next
            else:
                return False
        return True             

# Time Complexity: O(N) where N is the number of nodes
# Space Complexity: O(1) - in-place reversal
# Pattern: Slow/Fast Pointers + List Reversal
# Trick: Use fast/slow pointers to find middle. Reverse second half in place. Compare first half with reversed second half to check palindrome