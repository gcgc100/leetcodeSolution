#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    Intro
    """
    def plusOne(self, digits):
        n = int("".join(map(lambda x: str(x), digits))) + 1
        return map(lambda x:int(x), str(n))
