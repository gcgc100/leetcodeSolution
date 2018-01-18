#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):

    """Docstring for Solution. """

    def __init__(self):
        """init """
        pass

    def twoSum(self, nums, target):
        """

        :nums: TODO
        :target: TODO
        :returns: TODO

        """
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums[i+1:]):
                if v1 + v2 == target:
                    return [i, j+i+1]
