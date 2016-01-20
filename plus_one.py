#!/usr/bin/env python
# encoding: utf-8

"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits or len(digits)==0:
            return digits
        if len(digits)==1 and digits[0]==9:
            return [1,0]
        elif len(digits)>1 and digits[len(digits)-1]==9:
            return self.plusOne(digits[:-1])+[0]
        else:
            digits[len(digits)-1]+=1
            return digits

