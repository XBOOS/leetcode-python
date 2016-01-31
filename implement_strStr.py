#!/usr/bin/env python
# encoding: utf-8

"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack."""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle:
            return 0
        elif not needle:
            return 0
        elif not haystack:
            return -1

        start = walk = 0
        while (start+walk)<len(haystack) and walk<len(needle):
            if haystack[start+walk]!=needle[walk]:
                start +=1
                walk=0
            else:
                walk +=1
        if walk == len(needle):
            return start
        else:
            return -1


