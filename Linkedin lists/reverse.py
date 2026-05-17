# Problem: Reverse entire singly linked list iteratively
# Pattern: Iterative Reversal with Three Pointers - prev, cur, next
# Brute Force: Recursive approach - O(n) space on call stack
# Method: Use three pointers to reverse direction of next pointers as we traverse
# Time: O(n), Space: O(1) only pointer storage

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