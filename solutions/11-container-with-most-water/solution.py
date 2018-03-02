#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        curMaxArea = 0
        if len(height) == 2:
            return min(height)
        if len(height) < 2:
            return 0
        split = len(height)/2
        sh1 = height[0:split]
        sh2 = height[split:len(height)]
        print("sh1 %s" % sh1)
        print("sh2 %s" % sh2)
        curMaxArea = max(self.maxArea(sh1), self.maxArea(sh2))
        print(curMaxArea)
        for i in range(len(sh1)):
            for j in range(len(sh2)):
                h1 = sh1[i]
                h2= sh2[j]
                print("i,j:%s %s" % (i, j))
                area = min(h1, h2) * (j+split-i)
                print(area)
                if area > curMaxArea:
                    curMaxArea = area
                    print(curMaxArea)
        return curMaxArea
