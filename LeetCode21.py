# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        preHead = ListNode(-1)
        prev = preHead
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                prev = l1
                l1 = l1.next
            else:
                prev.next = l2
                prev = l2
                l2 = l2.next
        prev.next = l1 if l1 else l2
        return preHead.next

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(4)
    n4 = ListNode(1)
    n5 = ListNode(3)
    n6 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n4.next = n5
    n5.next = n6
    solution = Solution()
    solution.mergeTwoLists(n1, n4)