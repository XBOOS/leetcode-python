#!/usr/bin/env python
# encoding: utf-8

"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
Hint:

You should make use of what you have produced already.
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
Or does the odd/even status of the number help you in calculating the number of 1s?
"""
""" Method1. just trying and find the regular pattern of the array.
Just as the hint tells you."""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        if num==0:
            return res
        x = num
        times = 0
        while x>0:
            x /=2
            times+=1
        while times>0:
            times-=1
            res =res + [x+1 for x in res]

        return res[:num+1]

""" Method 2 using dynamic programming, not use the range,but even/odd as the divider """
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]*(num+1)
        for i in range(1,num+1):
            if i&0x01:
                res[i] = res[i-1]+1
            else:
                res[i] = res[i/2]
        return res
