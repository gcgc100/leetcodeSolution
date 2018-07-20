#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    Intro
    """
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        commonStr = strs[0]
        for s in strs[1:]:
            for i in range(len(commonStr),-1, -1):
                if s.startswith(commonStr[0:i]):
                    commonStr = commonStr[0:i]
                    break
                commonStr = commonStr[0:i]
            if commonStr == "":
                break
        return commonStr
