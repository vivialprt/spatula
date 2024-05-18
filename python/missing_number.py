"""
Solutions for Clone Graph problem
https://leetcode.com/problems/missing-number/
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Sum of n sequentials number can be found by a formula.
        Substracting the sum of provided numbers will
        return the missing number.
        """
        return (len(nums) * (len(nums) + 1) // 2) - sum(nums)
