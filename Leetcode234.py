from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        if fast:
            slow = slow.next
        while slow:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        return True

if __name__ == '__main__':
    solution = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    print(solution.isPalindrome(node1))