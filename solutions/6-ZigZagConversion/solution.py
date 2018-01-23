#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
    of rows like this: 

    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"
    Write the code that will take a string and make this conversion given a
    number of rows:

    string convert(string text, int nRows);
    convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
    """

    def convert(self, s, numRows):
        """

        :type s: str
        :type numRows: int
        :rtype: str

        """
        lineArray = [[] for i in range(numRows)]
        lineNum = -1
        colNum = 0
        for character in s:
            if colNum % 2 == 1:
                # odde column, step 2
                lineNum += 2
                lineArray[lineNum % numRows].append(character)
                if lineNum % numRows == 0 or lineNum % numRows == numRows-1:
                    # next column
                    colNum += 1
            else:
                # even column, step 1
                lineNum += 1
                lineArray[lineNum % numRows].append(character)
                if lineNum % numRows == numRows-1:
                    # next column
                    colNum += 1
            if lineNum % numRows == 0 or lineNum % numRows == numRows-1:
                # next column
                colNum += 1
        lineStrArray = ["".join(s) for s in lineArray]
        print lineStrArray
        return "".join(lineStrArray)
