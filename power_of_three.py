#!/usr/bin/env python
# encoding: utf-8

# No recursion and no loop
import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <=0:
            return False
        x = math.log(n,3)
        return abs(x-round(x))<1e-10

