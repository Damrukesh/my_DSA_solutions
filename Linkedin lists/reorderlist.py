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
# trick : reverse the second half of the list and then merge it with the first half of the list            



        