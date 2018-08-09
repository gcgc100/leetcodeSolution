#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

class Solution(object):
    """
    Intro
    """
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start+end)/2
            print "%s %s %s" % (start, end, mid)
            if mid == len(nums):
                return mid
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid -1
            else:
                start = mid + 1
        mid = int(math.ceil((start+end)/2.0))
        return mid
