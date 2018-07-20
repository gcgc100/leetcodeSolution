#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    Intro
    """

    def mergeTwoLists(self, l1, l2):
        i = j = 0
        result = []
        while i < len(l1) and j < len(l2):
            if l1[i] >= l2[j]:
                result.append(l2[j])
                j += 1
            if l1[i] <= l2[j]:
                result.append(l1[i])
                i += 1
        result.extend(l2[j:])
        result.extend(l1[i:])
        return result
