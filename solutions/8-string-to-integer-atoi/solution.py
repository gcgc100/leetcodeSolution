#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    Implement atoi to convert a string to an integer.
    This is not a problem in python.
    I will try to implement it in a c++ style
    """
    
    def myAtoi(self, strToConvert):
        """

        :type strToConvert: string
        :rtype : int

        """
        ret = 0
        sign = 1  # if positive
        try:
            i = 0
            while True:
                c = strToConvert[i]
                if c == " ":
                    i += 1
                    continue
                if i == 0:
                    if c == "-":
                        sign = -1
                        i += 1
                        continue
                    elif c == "+":
                        i += 1
                        continue
                num = ord(c) - 48
                if num > 9 or num < 0:
                    raise Exception()
                ret = ret*10 + num
                i += 1
        except IndexError:
            pass
        
        return ret * sign
        
