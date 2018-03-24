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

    # def convert(self, s, numRows):
    #     """

    #     :type s: str
    #     :type numRows: int
    #     :rtype: str

    #     """
    #     if numRows == 0:
    #         return
    #     flag = numRows - 1
    #     i = 0
    #     lineArray = []
    #     while i < len(s):
    #         if flag == numRows -1 or flag == 0:
    #             lineArray.append([x for x in s[i:i+numRows]])
    #             i = i + numRows
    #             flag = max(numRows - 2, 0)
    #         elif flag < numRows -1 and flag > 0:
    #             tempLine = [None for x in range(numRows)]
    #             tempLine[flag] = s[i]
    #             lineArray.append(tempLine)
    #             i = i+1
    #             flag = flag -1
    #     if len(lineArray) > 0:
    #         while len(lineArray[-1]) < numRows:
    #             lineArray[-1].append(None)
    #     else:
    #         return ""
    #     __import__("nose").tools.set_trace()

    #     lineArrayNew = [[row[col] for row in lineArray] for col in range(len(lineArray[0]))]
    #     for l in lineArrayNew:
    #         while True:
    #             try:
    #                 l.remove(None)
    #             except ValueError:
    #                 break
    #     return "".join(["".join(w) for w in lineArrayNew])

    def convert(self, s, numRows):
        """

        :type s: str
        :type numRows: int
        :rtype: str

        """
        i = 0
        retStr = ""
        while i < numRows:
            if i == 0 or i == numRows -1:
                index = i
                while index < len(s):
                    retStr += s[index]
                    index += max(2*numRows-2, 1)
            else:
                index = i
                while index < len(s):
                    retStr += s[index]
                    mid = index + 2*numRows -2*i - 2
                    if mid < len(s):
                        retStr += s[mid]
                    index += 2*numRows-2
            i += 1
        return retStr
