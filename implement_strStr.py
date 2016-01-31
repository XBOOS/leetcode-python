#!/usr/bin/env python
# encoding: utf-8

"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack."""

""" The first time I jump start by walk+1 but there are matching miss. So just should start from the next char
start +=1"""
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

# unlock the solution
"""
O(nm) runtime, O(1) space – Brute force:

You could demonstrate to your interviewer that this problem can be solved using known efficient algorithms such as Rabin-Karp algorithm, KMP algorithm, and the Boyer- Moore algorithm. Since these algorithms are usually studied in an advanced algorithms class, it is sufficient to solve it using the most direct method in an interview – The brute force method.

The brute force method is straightforward to implement. We scan the needle with the haystack from its first position and start matching all subsequent letters one by one. If one of the letters does not match, we start over again with the next position in the haystack.

The key is to implement the solution cleanly without dealing with each edge case separately."""

# It seems no edge cases needed
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

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


