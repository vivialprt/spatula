"""
Solutions for Pacific Atlantic Water Flow problem
https://leetcode.com/problems/pacific-atlantic-water-flow
"""
from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Solution with sets for remembering cells that end up
        in each ocean and stack for DFS for each ocean.
        """
        rows, cols = len(heights), len(heights[0])
        pacific_sources = set()
        atlantic_sources = set()
        pacific_stack = deque()
        atlantic_stack = deque()
        # Sets and stacks are initialized
        # with cells that touch oceans
        for i in range(rows):
            pacific_sources.add((i, 0))
            pacific_stack.append((i, 0))
            atlantic_sources.add((i, cols - 1))
            atlantic_stack.append((i, cols - 1))
        for j in range(cols):
            pacific_sources.add((0, j))
            pacific_stack.append((0, j))
            atlantic_sources.add((rows - 1, j))
            atlantic_stack.append((rows - 1, j))

        # Traversing pacific ocean
        while pacific_stack:
            i, j = pacific_stack.pop()

            # top, bottom, left, right neighbors
            for k, l in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                # check border violations
                if k < 0 or l < 0 or k >= rows or l >= cols:
                    continue

                if heights[i][j] <= heights[k][l]:
                    if (k, l) not in pacific_sources:
                        pacific_sources.add((k, l))
                        pacific_stack.append((k, l))

        # Traversing atlantic ocean
        while atlantic_stack:
            i, j = atlantic_stack.pop()

            # top, bottom, left, right neighbors
            for k, l in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                # check border violations
                if k < 0 or l < 0 or k >= rows or l >= cols:
                    continue

                if heights[i][j] <= heights[k][l]:
                    if (k, l) not in atlantic_sources:
                        atlantic_sources.add((k, l))
                        atlantic_stack.append((k, l))

        # Returning intersection of sets
        return atlantic_sources & pacific_sources
