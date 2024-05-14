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

    def cloneGraph2(self, node: Optional['Node']) -> Optional['Node']:
        """
        Depth-first traversing and hashmap utilization.
        """
        # Small heuristics can give boost for some test cases
        if node is None:
            return None

        if len(node.neighbors) == 0:
            return Node(node.val)

        # Stack for DFS traversing
        stack = deque()
        stack.append(node)

        # Hashmap for cloned nodes to avoid rebuilding the same nodes
        cloned = {}

        # Set of seen nodes,
        # so already seen nodes are not being pushed to stack.
        # We cannot use cloned hashmap for this,
        # because if node is cloned it does not mean it's been seen
        seen = {node}

        while stack:
            current_node = stack.pop()

            # If node is not cloned yet, we only recreate value,
            # without neighbors
            if current_node.val not in cloned:
                cloned[current_node.val] = Node(current_node.val)

            for neighbor in current_node.neighbors:
                # Neighbor has not been seen
                # add him to stack and mark as seen
                if neighbor not in seen:
                    stack.append(neighbor)
                    seen.add(neighbor)

                # Ensure the neighbor is cloned
                if neighbor.val not in cloned:
                    cloned[neighbor.val] = Node(neighbor.val)

                # Add the neighbor to the list of current node neighbors
                cloned[current_node.val].neighbors.append(cloned[neighbor.val])

        return cloned[1]


if __name__ == "__main__":
    solution = Solution()
    graph = solution.createGraph([[2, 4], [1, 3], [2, 4], [1, 3]])
    solution.printGraph(graph)
    clone = solution.cloneGraph2(graph)
    solution.printGraph(clone)
