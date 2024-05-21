"""
Solutions for Merge k Sorted Lists problem
https://leetcode.com/problems/merge-k-sorted-lists/
"""
import heapq
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Extention to support compare operator
# for compatability with heapq
class MyNode:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        """
        Solution with heap queue. All lists are being
        pushed to heap. Then, while heap is not empty
        the smallest list is being extracted, its top node
        pushed to resuting list, and list pushed back to heap.
        The heap is used for fast push and pop operations.
        """
        # start condition, this node is not used
        # but need to start with something with
        # the same interface
        head = ListNode()
        tail = head
        # Heapify lists excluding empty lists
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, MyNode(node))
        while heap:
            # extract smallest list (always first)
            temp = heapq.heappop(heap)
            tail.next = temp.node
            # if there are still nodes in list,
            # push list back to heap (fast, as heap is sorted)
            if temp.node.next:
                heapq.heappush(heap, MyNode(temp.node.next))

            tail = tail.next

        return head.next
