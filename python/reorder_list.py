"""
Solutions for Reorder List problem
https://leetcode.com/problems/reorder-list/
"""
from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Debug purposes
    def __repr__(self):
        return f"{self.val} -> {repr(self.next)}"

    # Debug purposes
    def __str__(self):
        return f"{self.val} -> {repr(self.next)}"


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        First all nodes pushed to stack, then list is being
        reordered until the middle is reached
        """
        left = right = head
        stack = deque()
        # Traverse list and put nodes to stack
        while right.next:
            stack.append(right)
            right = right.next
        # Reordering cycle till the middle of the list is reached.
        # Two checks for odd and even lists.
        while left.next != right and left != right:
            right.next = left.next
            left.next = right
            left = right.next
            right = stack.pop()
        # Null last nodes' next to avoid list cycles.
        right.next = None


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(head)
    sol.reorderList(head)
    print(head)
