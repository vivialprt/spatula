"""
Solutions for Clone Graph problem
https://leetcode.com/problems/clone-graph
"""
from typing import Optional, List
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def createGraph(self, edges=List[List[int]]) -> 'Node':
        """
        Create graph nodes from edge notation
        """
        nodes = {}
        for i in range(len(edges)):
            if i + 1 not in nodes:
                nodes[i + 1] = Node(val=i + 1)

            for neighbor in edges[i]:
                if neighbor not in nodes:
                    nodes[neighbor] = Node(val=neighbor)

                nodes[i + 1].neighbors.append(nodes[neighbor])

        return nodes[1]

    def printGraph(self, node: 'Node') -> None:
        """
        Traverse and print graph.
        """
        edges = {}
        stack = deque()
        stack.append(node)
        while stack:
            current_node = stack.pop()
            if current_node.val in edges:
                continue
            edges[current_node.val] = [
                neighbor.val
                for neighbor in current_node.neighbors
            ]
            stack.extend(current_node.neighbors)
        print(edges)

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Baseline
        """
        import copy
        return copy.deepcopy(node)


if __name__ == "__main__":
    solution = Solution()
    graph = solution.createGraph([[2, 4], [1, 3], [2, 4], [1, 3]])
    solution.printGraph(graph)
    clone = solution.cloneGraph(graph)
    solution.printGraph(clone)
