#!/usr/bin/env python
# encoding: utf-8
# Method 1
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 0:
            if n==1:
                return True
            elif n%2:
                return False
            n >>= 1

        return False
# Method 2
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <1:
            return False
        else:
            return n&(n-1)==0

