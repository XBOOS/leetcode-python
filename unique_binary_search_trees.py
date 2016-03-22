#!/usr/bin/env python
# encoding: utf-8

"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
Subscribe to see which companies asked this question

Hide Tags Tree Dynamic Programming
Show Similar Problems
"""
"""Using dynamic programming. bottom-up approach"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        chart = [0]*(1+n)
        chart[0]=1
        for i in range(1,n+1):
            for j in range(i):
                chart[i] += chart[j]*chart[i-j-1]
        return chart[n]

"""  Method 2 Recursion with memorization"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[-1]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][i] = 1

        def dfs(l,r):
            if l>r:
                return 0
            if dp[l][r]>=0:
                return dp[l][r]
            res = 0
            for mid in range(l,r+1):
                res = res+max(1,dfs(l,mid-1))*max(1,dfs(mid+1,r))
            dp[l][r] = res
            return res
        return dfs(1,n)
