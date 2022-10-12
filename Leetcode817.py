# Definition for singly-linked list.
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        ans = 0
        numSet = set(nums)
        while head:
            if head.val in numSet:
                while head and head.val in numSet:
                    head = head.next
                ans += 1
            else:
                head = head.next
        return ans


l1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
solution = Solution()
print(solution.numComponents(l1, [0, 1, 3]))
l2 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
print(solution.numComponents(l2, [0, 3, 1, 4]))
l3 = ListNode(0, ListNode(1, ListNode(2)))
print(solution.numComponents(l3, [0, 2]))