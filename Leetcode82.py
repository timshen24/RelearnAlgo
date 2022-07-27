# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1, head)
        cur = head
        prev = dummy
        nxt = cur.next
        while cur and nxt:
            if cur.val == nxt.val:
                while nxt and cur.val == nxt.val:
                    cur = cur.next
                    nxt = cur.next
                prev.next = nxt
                cur = nxt
                if cur:
                    nxt = cur.next
            else:
                prev = cur
                cur = cur.next
                nxt = cur.next
        return dummy.next


l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
solution = Solution()
print(solution.deleteDuplicates(l1).val)
l2 = ListNode(1, ListNode(1, None))
print(solution.deleteDuplicates(l2))
