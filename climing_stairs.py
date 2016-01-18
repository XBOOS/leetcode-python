#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0

        charts = [0]*(n)
        for i in range(n):
            if i==0:
                charts[i]=1
            elif i==1:
                charts[i]=2
            else:
                charts[i]=charts[i-1]+charts[i-2]
        return charts[n-1]
