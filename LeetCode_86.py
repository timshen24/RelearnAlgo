# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def partition(head: ListNode, x: int) -> ListNode:
    small_head, small_cur = None, None
    big_head, big_cur = None, None
    cur = head
    while cur is not None:
        if cur.val < x:
            if small_cur is None:
                small_head = cur
                small_cur = cur
            else:
                small_cur.next = cur
                small_cur = cur
        else:
            if big_cur is None:
                big_head = cur
                big_cur = cur
            else:
                big_cur.next = cur
                big_cur = cur
        cur = cur.next
    if small_cur is not None:
        small_cur.next = big_head
    return small_head

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n4 = ListNode(2)
    n5 = ListNode(5)
    n6 = ListNode(2)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    partition(n1, 3)
