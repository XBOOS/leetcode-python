#!/usr/bin/env python
# encoding: utf-8

"""
Implement pow(x, n)."""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0:
            return 0
        elif x==1:
            return 1.0
        elif x==-1:
            if n%2==0:
                return 1.0
            else:
                return -1.0
        elif n==0:
            return 1.0
        elif n<0:
            n*=(-1)
            x**=(-1)
        power = 1
        while n>0 and abs(power)>=0.00000000001:
            n-=1
            power*=x
        return power
