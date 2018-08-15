#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    Intro
    """
    def addBinary(self, a, b):
        return "{0:b}".format(int(a,2) + int(b,2))
