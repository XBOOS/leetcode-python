#!/usr/bin/env python
# encoding: utf-8

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"."""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = [[]for _ in xrange(numRows)]
        rowCycle = [x for x in range(numRows)]+[x for x in range(1,numRows-1)][::-1]
        i = 0
        for ss in s:
            row = rowCycle[i]
            res[row].append(ss)
            i = (i+1)%len(rowCycle)

        return "".join(["".join(x) for x in res])

