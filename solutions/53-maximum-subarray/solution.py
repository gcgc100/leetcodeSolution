#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    Intro
    """
    def maxSubArray(self, nums):
        if not nums:
            return None
        maxSum = nums[0]
        curMax = nums[0]
        for i in range(1, len(nums)):
            curMax = max(curMax + nums[i], nums[i])
            maxSum = max(maxSum, curMax)
        return maxSum
