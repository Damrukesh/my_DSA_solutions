# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        a=head
        prev=None      
        while a:
            cur=a
            a=cur.next
            cur.next=prev
            prev=cur
        return prev

# Time Complexity: O(N) where N is the number of nodes in the linked list
# Space Complexity: O(1) - only using a few pointers
# Pattern: Iterative Reversal with Three Pointers
# Trick: Use three pointers (prev, cur, next) to reverse the list in place by changing the direction of next pointers