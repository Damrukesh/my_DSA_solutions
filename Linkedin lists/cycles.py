
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        s=set()
        while cur:
            if cur in s:
                return cur
            s.add(cur)
            cur=cur.next
             
# tro detect cycle without extra space we can use two pointers one slow and one fast
# we move slow by one step and fast by two steps if there is a cycle they will
        