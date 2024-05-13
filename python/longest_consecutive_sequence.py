"""
Solutions for Longest Consecutive Sequence problem
https://leetcode.com/problems/longest-consecutive-sequence
"""
from typing import List


class Solution:
    """
    Solution with the two mutually connected dicts
    for storing indexes of consecutive sequences,
    one maps start index to end index and one vice versa.
    Each number in input list is either:
    1) can be used to link two existing sequences
    2) can be used to extend existing sequences from start or from end
    3) can be used to start new sequence
    After updating existing sequence its new length is checked
    if it is bigger than current max length.
    Complexity is O(n), but many operations with dicts
    give a huge overhead.
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        # small heuristic can give boost for some test cases
        if len(nums) < 2:
            return len(nums)

        start_to_end = {}
        end_to_start = {}
        maxlen = 1

        # Set for skipping already visited numbers
        seen = set()
        for num in nums:
            if num in seen:
                continue
            else:
                seen.add(num)

            # num is between two existing sequences
            # i.e. sequences [1, 2] and [4] already present
            # and num is 3
            if (num + 1 in start_to_end) and (num - 1 in end_to_start):
                # merge seqs
                start = end_to_start[num - 1]
                end = start_to_end[num + 1]
                del start_to_end[num + 1]
                del end_to_start[num - 1]
                start_to_end[start] = end
                end_to_start[end] = start
                if end - start + 1 > maxlen:
                    maxlen = end - start + 1

            # num can extend existing sequence from end
            # i.e sequence [1, 2] is present and num is 3
            elif num + 1 in start_to_end:
                # extend seq
                end = start_to_end[num + 1]
                del start_to_end[num + 1]
                start_to_end[num] = end
                end_to_start[end] = num
                if end - num + 1 > maxlen:
                    maxlen = end - num + 1

            # num can extend existing sequence from start
            # i.e sequence [1, 2] is present and num is 0
            elif num - 1 in end_to_start:
                # extend seq
                start = end_to_start[num - 1]
                del end_to_start[num - 1]
                end_to_start[num] = start
                start_to_end[start] = num
                if num - start + 1 > maxlen:
                    maxlen = num - start + 1

            # num is too far from any existent sequence
            # so new sequence [num: num] is created
            else:
                # create seq
                start_to_end[num] = num
                end_to_start[num] = num

        return maxlen

    def longestConsecutive2(self, nums: List[int]) -> int:
        """
        Solution with presorting. First, duplicates
        are bieng removed from nums, then nums are sorted.
        Nums are iterated and if two nums are consecutive,
        temporary consequtives counter is incremented, else
        counter is reset and checked if it is bigger than
        current max length. The check is also performed
        after loop, because the counter might not be reset.
        Complexity is O(nlogn) for sorting and O(n) for loop.
        """
        # small heuristic can give boost for some test cases
        if len(nums) < 2:
            return len(nums)
        temp = 1
        maxlen = 1
        nums = sorted(set(nums))
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                temp += 1
            else:
                if temp > maxlen:
                    maxlen = temp
                temp = 1
        if maxlen > temp:
            return maxlen
        else:
            return temp
