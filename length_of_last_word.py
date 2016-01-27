#!/usr/bin/env python
# encoding: utf-8

"""

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return

careful that the spaces at the end of the string"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        i=len(s)-1
        length = 0
        while i>=0 and s[i]==' ':
            i -= 1
        while i>=0:
            if s[i] == ' ':
                return length
            else:
                length +=1
            i-=1
        return length

