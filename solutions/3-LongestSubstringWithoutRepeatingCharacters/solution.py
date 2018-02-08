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
        for start in range(len(s)+1):
            for end in range(start+1, len(s)+1):
                length = end - start
                if length < longestLen:
                    continue
                if len(set(list(s[start:end]))) < length:
                    break
                else:
                    longestLen = length
        return longestLen
