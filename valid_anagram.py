#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        record = [0]*26
        for ss in s:
            record[ord(ss)-97] += 1
        for tt in t:
            record[ord(tt)-97] -= 1

        return all([r==0 for r in record])

