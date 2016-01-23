#!/usr/bin/env python
# encoding: utf-8

"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1]."""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #maintain two levels

        row = 2
        previous = [1,1]
        current = [1]
        if rowIndex < 0:
            return []
        elif rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            while row < rowIndex+1:
                for k in range(1,row):
                    current.append(previous[k-1]+previous[k])
                current.append(1)
                row += 1
                previous = current[:]
                current = [1]
            return previous



