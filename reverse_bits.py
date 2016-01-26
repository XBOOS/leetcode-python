#!/usr/bin/env python
# encoding: utf-8

"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

"""
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = list()
        for i in range(32):
            nums.append(n%2)
            n >>= 1

        newNum = 0
        for i in range(32):
            newNum <<= 1
            newNum += nums[i]
        return newNum


#Reduced to one loop
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        newNum = 0
        for i in range(32):
            newNum <<=1
            newNum += n%2
            n >>= 1

        return newNum

    # Method 2 use & and |
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        newNum = 0
        for i in range(32):
            newNum <<=1
            newNum |= (n>>i)&0x1

        return newNum

    #Method3 pythonic way to use string and built-in functions


