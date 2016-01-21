#!/usr/bin/env python
# encoding: utf-8

"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = list()
        for i in range(numRows):
            result.append([1]*(1+i))
            if i>1:
                for j in range(1,i):
                    result[i][j] = result[i-1][j-1]+result[i-1][j]
        return result
