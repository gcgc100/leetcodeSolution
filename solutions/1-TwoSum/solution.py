#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):

    """
    Given an array of integers, return indices of the two numbers such 
    that they add up to a specific target.
    """

    def __init__(self):
        """init """
        pass

    def twoSum(self, nums, target):
        """

        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        """
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums[i+1:]):
                if v1 + v2 == target:
                    return [i, j+i+1]
