#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

class Solution(object):
    """
    Intro
    """
    
    def isValid(self, s):
        qi = collections.deque()
        parenthesesPairs = [["(", ")"], ["{", "}"], ["[", "]"]]
        openParentheses = [x[0] for x in parenthesesPairs]
        closeParentheses = [x[1] for x in parenthesesPairs]
        for c in s:
            if c in openParentheses:
                qi.append(c)
            elif c in closeParentheses:
                expectParentheses = openParentheses[closeParentheses.index(c)]
                if qi and qi[-1] == expectParentheses:
                    qi.pop()
                else:
                    return False
            else:
                return False
        if not qi:
            return True
        return False
