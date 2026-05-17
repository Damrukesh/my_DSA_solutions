# Problem: Reverse nodes in groups of k, with last incomplete group left as-is
# Pattern: Iterative Reversal in Groups with Dummy Node - Process k nodes at a time
# Brute Force: Recursion to process groups - O(n) space on call stack
# Method: Use dummy node, reverse k nodes, reconnect, move to next group
# Time: O(n), Space: O(1) only pointer storage

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