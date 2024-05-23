"""
Solutions for Find Minimum in Rotated Sorted Array problem
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Solution by iteratively dividing list into
        subsequences. After division there are
        start and end of each part which are
        used to understand which part contains
        the minimum. Further, if smaller part is
        sorted (start is smaller than end) start
        is the minimum
        """
        subseq = nums
        while len(subseq) > 2:
            center = len(subseq) // 2
            # For each part find min in start and end
            left_min = min(subseq[0], subseq[center])
            right_min = min(subseq[center + 1], subseq[-1])

            if left_min < right_min:
                # if start < end, subseq is sorted
                if subseq[0] < subseq[center]:
                    return subseq[0]
                subseq = subseq[:center + 1]
            else:
                # if start < end, subseq is sorted
                if subseq[center + 1] < subseq[-1]:
                    return subseq[center + 1]
                subseq = subseq[center + 1:]
        return min(subseq)
