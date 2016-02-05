#!/usr/bin/env python
# encoding: utf-8
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]"""

""" Method 1. Idea based on the best time to sell and buy stock II.
when have to cool down, just compare the last addition,present addition, and two consecutive addtion plus the negation in between"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        daysNum = len(prices)
        profit = 0
        up_marker = 0
        down_marker = 0
        cooldown = False
        for i in range(1,daysNum):
            tmp = prices[i]-prices[i-1]
            if tmp>0:
                if cooldown:
                    profit = (profit-up_marker)+max(tmp,up_marker,up_marker+tmp+down_marker)
                    cooldown = False
                elif not cooldown:
                    profit +=tmp
            else:
                if i>1:
                    cooldown = not cooldown
                    up_marker = prices[i-1]-prices[i-2]
                    down_marker = prices[i]-prices[i-1]

        return profit


# I am on my way back home to celebrate the Chinese lunar new year.
# No access to online judge, so I just write the tests by myself.
# Testing

if __name__ =="__main__":
    print "Happy new year!"
    solution = Solution()
    prices = [1,2,3,1,6,7]
    print solution.maxProfit(prices)," should be 7"
    prices = [1,3,2,5,7]
    print solution.maxProfit(prices)," should be 6"
