#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class Solution(object):
    """
    Given a 32-bit signed integer, reverse digits of an integer.
    """

    def reverse(self, x):
        """

        :type x: int
        :rtype: int

        """
        ret = int("".join(reversed(str(abs(x)))))
        # tx = abs(x)
        # splitInt = []
        # while tx != 0:
        #     digit = tx % 10
        #     splitInt.append(digit)
        #     tx = tx / 10
        # weight = 1
        # ret = 0
        # for d in reversed(splitInt):
        #     ret  += weight * d
        #     weight = weight * 10
        if x < 0:
            ret = ret * -1
        return ret
