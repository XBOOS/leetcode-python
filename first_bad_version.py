#!/usr/bin/env python
# encoding: utf-8

"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binarySearch(1,n)
    def binarySearch(self,l,r):
        if l>r:
            return -1
        elif l==r:
            return l
        elif l+1==r:
            if isBadVersion(l):
                return l
            else:
                return r
        i = (l+r)/2

        if isBadVersion(i):
            return self.binarySearch(l,i)
        else:
            return self.binarySearch(i,r)