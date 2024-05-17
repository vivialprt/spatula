"""
Solutions for Clone Graph problem
https://leetcode.com/problems/linked-list-cycle
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional["ListNode"]) -> bool:
        """
        Solution with tortoise and hare algorithm.
        """
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False
