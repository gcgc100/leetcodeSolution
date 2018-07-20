#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

class Solution(object):
    """
    Intro
    """

    def __init__(self):
        """TODO: Docstring for init.
        :returns: TODO

        """
        self.symbols = ["I", "V", "X", "L", "C", "D", "M"]
        self.repeatSymbols = ["I", "X", "C", "M"]
        self.symbolWeight = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    def romanToInt(self, s):
        """Roman to integer

        :s: TODO
        :returns: TODO

        """
        romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
        prev_value = running_total =0
        for i in range(len(s)-1, -1, -1):
            int_val = romans[s[i]]
            if int_val < prev_value:
                running_total -= int_val
            else:
                running_total += int_val
                prev_value = int_val
            print running_total
        return running_total


    def romanToIntMine(self, s):
        """Roman to integer

        :s: string roman number
        :returns: TODO

        """
        result = 0
        qi = collections.deque()
        nextExpect = None
        for i, n in enumerate(s):
            if qi:
                if qi[-1] == n:
                    assert n in self.repeatSymbols
                    qi.append(n)
                elif qi[-1] == self.previousOne(n):
                    assert len(qi) == 1
                    result += self.symbolWeight[n] - self.symbolWeight[qi[-1]]
                    if qi[-1] == "I":
                        nextExpect = "I"
                    else:
                        nextExpect = qi[-1]
                    qi.clear()
                elif self.symbols.index(n) < self.symbols.index(qi[-1]):
                    result += self.symbolWeight[qi[-1]] * len(qi)
                    nextExpect = n
                    qi.clear()
                    qi.append(n)
            else:
                if nextExpect is None or self.symbols.index(n) < self.symbols.index(nextExpect):
                    qi.append(n)
                else:
                    assert False
        if qi:
            result += self.symbolWeight[qi[-1]] * len(qi)
        return result


    def previousOne(self, n):
        """Return the previous available one V->I,  C->X, I->None

        :n: TODO
        :returns: TODO

        """
        if n == "I":
            return None
        w = self.symbolWeight[n]
        while w > 10:
            w = w/10
        if w == 5:
            return self.symbols[self.symbols.index(n)-1]
        else:
            return self.symbols[self.symbols.index(n)-2]
