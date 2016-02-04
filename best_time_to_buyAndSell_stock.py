#!/usr/bin/env python
# encoding: utf-8

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        daysNum = len(prices)
        if daysNum==0:
            return 0

        mins =[0]*daysNum
        mins[0] = prices[0]
        maxs = [0]*daysNum
        maxs[-1] = prices[-1]
        for i in range(1,daysNum):
            if prices[i]<mins[i-1]:
                mins[i] = prices[i]
            else:
                mins[i] = mins[i-1]
        for i in (range(daysNum-1)[::-1]):
            if prices[i]>maxs[i+1]:
                maxs[i] = prices[i]
            else:
                maxs[i] = maxs[i+1]
        profit = 0
        for j in range(daysNum):
            profit =max(profit,(maxs[j]-mins[j]))
        return profit


    """Method 2, only take care of the profit and maintain the lowest price till now"""
 class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        daysNum = len(prices)
        if daysNum==0:
            return 0
        minTillNow = prices[0]
        profit = 0

        for i in range(1,daysNum):
            profit = max(profit,prices[i]-minTillNow)
            minTillNow = min(minTillNow,prices[i])

        return profit

