#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):

    """
    Given a string, return the length of the longest substring without
    repeating characters.
    """

    def __init__(self):
        """init """
        pass

    def lengthOfLongestSubstring(self, s):
        """

        :type s: str
        :rtype: int

        """
        longestLen = 0
        for i, v1 in enumerate(s):
            subStrList = [v1]
            curLen = 1
            for v2 in s[i+1:]:
                if v2 in subStrList:
                    if longestLen < curLen:
                        longestLen = curLen
                    break
                else:
                    subStrList.append(v2)
                    curLen += 1
        return longestLen
