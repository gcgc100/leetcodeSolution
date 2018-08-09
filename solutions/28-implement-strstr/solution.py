#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    Intro
    """
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        n = len(needle)
        m = len(haystack)

        for i in range(m-n+1):
            if haystack[i: i+n] == needle:
                return i

        return -1
