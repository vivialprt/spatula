"""
Solutions for Maximum Product Subarray problem
https://leetcode.com/problems/maximum-product-subarray/
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        This solution checks all possible consequent products
        and uses hashmap for storing intermediate results
        """
        result = nums[0]
        products_store = {}

        # Put all values to product store
        # and check if there is zeros and
        # how many negative numbers are there
        contain_zeros = False
        negative_count = 0
        total_product = 1
        for i in range(len(nums)):
            products_store[(i, i)] = nums[i]
            total_product *= nums[i]
            if nums[i] == 0:
                contain_zeros = True
            elif nums[i] < 0:
                negative_count += 1
            if nums[i] > result:
                result = nums[i]

        # Quick return if no zeros and even count of negatives
        if (not contain_zeros) and (negative_count % 2 == 0):
            return total_product

        # Iterate through window sizes, from 2 to the whole array
        for window_size in range(2, len(nums) + 1):
            for offset in range(len(nums) - window_size + 1):
                # new product consist of product of numbers from smaller window
                # and new number from current window
                new_product = products_store[(offset, offset + window_size - 2)] * nums[offset + window_size - 1]  # noqa: E501
                products_store[(offset, offset + window_size - 1)] = new_product  # noqa: E501
                # intermediate values are deleted to free memory
                del products_store[(offset, offset + window_size - 2)]
                if new_product > result:
                    result = new_product

        return result
