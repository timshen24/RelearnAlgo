# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head

        p1, p2 = dummy, dummy
        for i in range(n + 1):
            p1 = p1.next
        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    solution = Solution()
    solution.removeNthFromEnd(n1, 2)
