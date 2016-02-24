#!/usr/bin/env python
# encoding: utf-8

"""

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

"""

""" This solution is too slow!!!!"""
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return [0]
        visited = list()
        visited.append("0"*n)
        trap = list()
        while len(visited) < 2**n:
            pre = visited[-1]
            cur = pre[:]
            i = 0
            while i<n:
                if cur[i]=="0":
                    cur=cur[:i]+"1"+cur[i+1:]
                else:
                    cur=cur[:i]+"0"+cur[i+1:]
                if cur not in visited and cur not in trap:
                    visited.append(cur)
                    trap.append(cur)
                    break
                else:
                    cur = pre[:]
                i+=1
            if i==n: # traversed the possibility,go backtracking
                visited.pop()

        return [int(x,2) for x in visited]



    """ the OJ can only detect one, so try next order of change"""
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return [0]
        visited = list()
        visited.append("0"*n)
        trap = list()
        while len(visited) < 2**n:
            pre = visited[-1]
            cur = pre[:]
            i = n-1
            while i>=0:
                if cur[i]=="0":
                    cur=cur[:i]+"1"+cur[i+1:]
                else:
                    cur=cur[:i]+"0"+cur[i+1:]
                if cur not in visited and cur not in trap:
                    visited.append(cur)
                    trap.append(cur)
                    break
                else:
                    cur = pre[:]
                i-=1
            if i==-1: # traversed the possibility,go backtracking
                visited.pop()

        return [int(x,2) for x in visited]
