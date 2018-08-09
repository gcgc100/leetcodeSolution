#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    Intro
    """
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)
        flag = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[flag]:
                continue
            else:
                flag += 1
                nums[flag] = nums[i]
        for n in range(flag+1, len(nums)):
            nums.pop(flag+1)
        return flag+1
