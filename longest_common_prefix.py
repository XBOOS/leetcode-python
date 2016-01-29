#!/usr/bin/env python
# encoding: utf-8

"""
Write a function to find the longest common prefix string amongst an array of strings."""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs or strs==[]:
            return ""
        minlen = min([len(str) for str in strs])
        res = ""
        dummy = strs[0]

        for i in xrange(minlen):
            record = dummy[i]
            for j in range(len(strs)):
                if strs[j][i]!=record:
                    return res
            res+=record
        return res
