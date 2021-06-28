from queue import PriorityQueue
from unittest import TestCase


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(self, lists):
    dummy = ListNode(None)
    curr = dummy
    q = PriorityQueue()
    for node in lists:
        if node: q.put((node.val, node))
    while q.qsize() > 0:
        curr.next = q.get()[1]
        curr = curr.next
        if curr.next: q.put((curr.next.val, curr.next))
    return dummy.next


class Test(TestCase):
    def test_merge_klists(self):
        node1 = ListNode(0)
        result_tail = node1
        result_tail.next = ListNode(2)
        result_tail = result_tail.next
        result_tail.next = ListNode(4)
        result_tail = result_tail.next

        node2 = ListNode(1)

        node = mergeKLists(self, [node1, node2])
        while node:
            print(node.val)
            node = node.next
