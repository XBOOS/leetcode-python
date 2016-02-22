#!/usr/bin/env python
# encoding: utf-8

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        daysNum = len(prices)
        if daysNum <2:
            return 0
        if k>=daysNum:
            return self.maxProfit2(prices)

        globals = [[0]*(k+1) for i in range(daysNum)]
        locals = [[0]*(k+1) for i in range(daysNum)]

        for i in range(1,daysNum):
            for j in range(1, k+1):
                diff = prices[i]-prices[i-1]
                locals[i][j] = max(globals[i-1][j-1],locals[i-1][j]+diff)
                globals[i][j] = max(locals[i][j],globals[i-1][j])

        return globals[-1][-1]

    def maxProfit2(self,prices):
        maxProfit = 0
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1]>0:
                maxProfit +=prices[i]-prices[i-1]

        return maxProfit
