#!/usr/bin/env python
# encoding: utf-8

"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321"""
"""
The key is to deal with the sign and different boundary for negative and positive
not using long, so check, (maxint-tmp/10) with the high order value"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=0
        if x<0:
            flag = -1
            x = -x
        else:
            flag = 1

        res = 0
        while x>0:
            # tmp = res*10+x%10 -- already run over the intmax, not good
            tmp  = x%10
            if flag and res>(2**31-1-tmp)/10:
                return 0
            elif not flag and (res>2**31-tmp)/10:
                return 0
            res = tmp+res*10
            x/=10
        return res*flag
