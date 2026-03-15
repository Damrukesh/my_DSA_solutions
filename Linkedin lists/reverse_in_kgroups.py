class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        lastend = dummy
        laststart = head
        while True:
            cur = laststart
            knode = self.getk(cur, k)
            if not knode:
                break
            nextgroup = knode.next
            knode.next = None
            a = laststart
            prev = None
            while a:
                cur = a
                a = cur.next
                cur.next = prev
                prev = cur
            lastend.next = prev
            lastend = laststart
            laststart = nextgroup
        lastend.next = laststart
        return dummy.next
    def getk(self, cur, k):
        while cur and k > 1:
            cur = cur.next
            k -= 1
        return cur
# Time Complexity: O(N) where N is the number of nodes in the linked list
# Space Complexity: O(1) - only using a few pointers
# Pattern: Iterative Reversal in Groups with Dummy Node
# Trick: Use a dummy node to simplify edge cases. For each group of k nodes, reverse them in place and connect the reversed group back to the main list. Use a helper function to find the k-th node for each group.