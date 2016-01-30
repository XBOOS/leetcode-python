#!/usr/bin/env python
# encoding: utf-8

"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a,base=2)+int(b,base=2)))[2:]


# method 2 without the help of python built-in method
# be careful of the last carry value
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        i = len(a)-1
        j = len(b)-1
        res = ""
        while i>=0 and j>=0:
            sum = 0
            if a[i]=="1":
                sum+=1
            if b[j]=="1":
                sum+=1
            sum +=carry
            carry = sum/2
            res = str(sum%2)+res
            i-=1
            j-=1
        while i>=0:
            sum = 0
            if a[i]=="1":
                sum+=1
            sum +=carry
            carry = sum/2
            res = str(sum%2)+res
            i-=1
        while j>=0:
            sum = 0
            if b[j]=="1":
                sum+=1
            sum +=carry
            carry = sum/2
            res = str(sum%2)+res
            j-=1
        if carry>0:
            res = str(carry)+res
        return res

