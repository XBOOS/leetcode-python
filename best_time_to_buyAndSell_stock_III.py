#!/usr/bin/env python
# encoding: utf-8

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        daysNum = len(prices)
        if daysNum<2:
            return 0

        profits1 = [0]*daysNum
        profits2 = [0]*daysNum
        minTillNow = prices[0]
        maxTillNow = prices[daysNum-1]
        for i in range(1,daysNum):
            profits1[i] = max(profits1[i-1],prices[i]-minTillNow)
            minTillNow = min(minTillNow,prices[i])

        for i in (range(daysNum-1)[::-1]):
            profits2[i] = max(profits2[i+1],maxTillNow-prices[i])
            maxTillNow = max(maxTillNow,prices[i])
        maxProfit = 0
        for i in range(daysNum):
            maxProfit = max(maxProfit,profits1[i]+profits2[i])
        return maxProfit
