#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    Intro
    """
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = filter(lambda x: x!="", s.split(" "))
        if not l:
            return 0
        return len(l[-1])
