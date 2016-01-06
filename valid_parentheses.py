#!/usr/bin/env python
# encoding: utf-8

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack)<1:
                    return False
                elif not stack.pop()+c in ["()","[]","{}"]:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
