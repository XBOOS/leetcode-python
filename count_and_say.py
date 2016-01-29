#!/usr/bin/env python
# encoding: utf-8

"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string."""
# spend a lot of time debugging. Pretty bad
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        tmp = "1"
        while n>1:
            result = ""
            prev = tmp[0]
            sum = 1
            i = 1
            while i<len(tmp):
                if tmp[i]==prev:
                    sum+=1
                else:
                    result +=(str(sum)+str(prev))
                    prev = tmp[i]
                    sum=1
                i+=1
            result +=(str(sum)+str(prev))
            tmp = result
            n-=1
        return tmp

