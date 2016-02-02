#!/usr/bin/env python
# encoding: utf-8

"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1s = [int(x) for x in version1.split(".")]
        v2s = [int(x) for x in version2.split(".")]
        if len(v1s)<len(v2s):
            for _ in range(len(v2s)-len(v1s)):
                v1s.append(0)
        elif len(v1s)>len(v2s):
            for _ in range(len(v1s)-len(v2s)):
                v2s.append(0)

        i=0
        while i<len(v1s):
            if v1s[i]>v2s[i]:
                return 1
            elif v1s[i]<v2s[i]:
                return -1
            else:
                i+=1
        return 0
