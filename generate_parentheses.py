#!/usr/bin/env python
# encoding: utf-8

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
"""
# "((()))", "(()())", "(())()", "()(())", "()()()"


"""
Backtracking, basically to enumerate all possible results and apply pruning to make it faster
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        cur = list()
        cur.append("(")
        i = 1
        while i<n*2:
            k = len(cur)
            while k>0:
                pre = cur[0]
                del cur[0]
                numOfLeft = sum([1 for cc in pre if cc=="("])
                if numOfLeft< n:
                    cur.append(pre+"(")
                if numOfLeft>(len(pre)-numOfLeft):
                    cur.append(pre+")")
                k-=1
            i+=1

        return cur

