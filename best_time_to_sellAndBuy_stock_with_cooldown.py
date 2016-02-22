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



"""Only the right solution, with help of two auxiliary arrays buys and sells.
buys means that the max profits with hold of today's stock
sells means that the max profits till now without hold of today's stock"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        daysNum = len(prices)
        if daysNum <2:
            return 0
        buys = [0]*(daysNum)
        sells = [0]*(daysNum)

        buys[0] = -prices[0]
        buys[1] = max(-prices[0],-prices[1])

        sells[1] = max(prices[1]-prices[0],0)

        #status tranformation
        for i in range(2,daysNum):
            buys[i] = max(buys[i-1],sells[i-2]-prices[i])
            sells[i] = max(buys[i-1]+prices[i],sells[i-1])

        return sells[-1]


"""
solution's below are not correct, but it pass my tests which obviously passes not all the situations
"""
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

"""  Method 2, from another point of view, instead of based on daily price,
based on the change of prices during the slot between different days.
when the change is positive, then the price goes up. when the change is negative,
then the price goes down.
So in best_time_toBuyANdSell_II, just add all the positive numbers together to get the max.
heere the each slot must have two between them"""
class Solution1(object):
    def maxProfit(self,prices):
        """
        :type prices: List[int]
        :rtype: int"""

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
