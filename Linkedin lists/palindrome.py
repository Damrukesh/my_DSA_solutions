# Problem: Check if linked list is palindrome
# Pattern: Slow/Fast Pointers + List Reversal - Find middle, reverse second half, compare
# Brute Force: Convert to array and check palindrome - O(n) space
# Method: Use fast/slow pointers to find middle, reverse second half, compare both halves
# Time: O(n), Space: O(1) in-place

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