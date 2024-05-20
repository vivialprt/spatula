"""
Solutions for Merge Two Sorted Lists problem
https://leetcode.com/problems/merge-two-sorted-lists/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional["ListNode"],
        list2: Optional["ListNode"]
    ) -> Optional["ListNode"]:
        """
        Iteratively take nodes from each list
        and compare them. Node with smaller
        value is removed from its' list and
        being inserted to resulting list.
        """
        head = ListNode()
        tail = head
        while list1 or list2:
            # If both lists have nodes
            if list1 and list2:
                if list1.val <= list2.val:
                    tail.next, list1 = list1, list1.next
                else:
                    tail.next, list2 = list2, list2.next
                tail = tail.next
                continue
            # If first list has nodes
            elif list1:
                tail.next = list1
            # If second list has nodes
            elif list2:
                tail.next = list2
            return head.next
