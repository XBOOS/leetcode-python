#!/usr/bin/env python
# encoding: utf-8

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
