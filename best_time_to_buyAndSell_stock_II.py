#!/usr/bin/env python
# encoding: utf-8

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again)."""

"""buy all the hill climing parts. """
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        daysNum = len(prices)
        if daysNum<2:
            return 0

        profit = 0
        for i in range(1,daysNum):
            if prices[i]>prices[i-1]:
                profit += (prices[i]-prices[i-1])
        return profit
