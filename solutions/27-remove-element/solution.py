#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    Intro
    """
    def removeElement(self, nums, val):
        flag = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[flag] = nums[i]
                flag += 1
        return flag
