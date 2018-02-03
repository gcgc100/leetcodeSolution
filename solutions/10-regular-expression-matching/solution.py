#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    Intro
    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

    The matching should cover the entire input string (not partial).

    The function prototype should be:
    bool isMatch(const char *s, const char *p)

    Some examples:
    isMatch("aa","a") → false
    isMatch("aa","aa") → true
    isMatch("aaa","aa") → false
    isMatch("aa", "a*") → true
    isMatch("aa", ".*") → true
    isMatch("ab", ".*") → true
    isMatch("aab", "c*a*b") → true
    """

    def isMatch(self, s, p):
        """

        :type s: str
        :type p: str
        :rtype: bool

        """
        print s
        print p
        print "----------"
        if p == "":
            if s == "":
                return True
            else:
                return False
        if len(p) > 1:
            if p[1] == "*":
                if p[0] == "*":
                    raise Exception()
                elif p[0] == ".":
                    if len(p) == 2:
                        return True
                    i = 0
                    while i < len(s):
                        if self.isMatch(s[i:], p[2:]):
                            return True
                        i += 1
                    return self.isMatch(s[i:], p[2:])
                else:
                    i = 0
                    if len(p) == 2:
                        while i < len(s):
                            if s[i] != p[0]:
                                return False
                            i += 1
                        return True
                    while i < len(s):
                        if self.isMatch(s[i:], p[2:]):
                            return True
                        if s[i] != p[0]:
                            return False
                        i += 1
                    return self.isMatch(s[i:], p[2:])
            else:
                if s == "":
                    return False
                if p[0] == "." or s[0] == p[0]:
                    return self.isMatch(s[1:], p[1:])
                else:
                    return False
        else:
            if p[0] == "*":
                raise Exception()
            if p[0] == ".":
                if len(s) == 1:
                    return True
                else:
                    return False
            else:
                if s == p:
                    return True
                else:
                    return False
