#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    Intro
    """
    def countAndSay(self, n):
        if n == 1:
            return "1"
        s = self.countAndSay(n-1)
        start = 0
        retStr = ""
        for i in range(len(s)):
            if s[i] == s[start]:
                continue
            else:
                retStr = "%s%s%s" % (retStr, i-start, s[start])
                start = i
        retStr = "%s%s%s" % (retStr, len(s)-start, s[start])
        return retStr
