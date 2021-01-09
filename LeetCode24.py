# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
    #     hair=ListNode(0,head)
    #     p=head
    #     pre=hair
    #     while p and p.next:
    #         nxt=p.next.next
    #         pre.next=p.next
    #         p.next.next=p
    #         p.next=nxt
    #         pre=p
    #         p=nxt
    #     return hair.next
        hair = ListNode(0, head)
        prev = hair
        while head and head.next:
            nxt = head.next.next
            prev.next = head.next.next
            head.next.next = head
            head.next = nxt
            prev = head
            head = nxt
        return hair.next


solution = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
print(solution.swapPairs(n1))