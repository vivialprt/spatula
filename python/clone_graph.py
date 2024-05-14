"""
Solutions for Clone Graph problem
https://leetcode.com/problems/clone-graph
"""
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Baseline
        """
        import copy
        return copy.deepcopy(node)
