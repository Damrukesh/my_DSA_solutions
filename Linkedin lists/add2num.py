# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        cur=dummy
        carry=0
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0 
            res=v1+v2+carry
            cur.next=ListNode(res%10)
            carry=res//10
            cur=cur.next
            if l1:l1=l1.next 
            if l2:l2=l2.next 
        return dummy.next     

# Time Complexity: O(max(L1, L2)) where L1 and L2 are lengths of the two linked lists
# Space Complexity: O(max(L1, L2)) for the result list
# Pattern: Linked List Traversal with Arithmetic
# Trick: Traverse both lists simultaneously, sum values with carry, create new node with (sum % 10), propagate carry to next iteration. Handle different lengths and final carry