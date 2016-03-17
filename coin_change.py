#!/usr/bin/env python
# encoding: utf-8

"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

"""
"""
Method1 Iterative solution.
THis should be right. but too slow because of python. Dangerously just crossing the time line"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        d = [amount+1]*(amount+1)
        d[0] = 0
        for i in xrange(1,amount+1):
            for coin in coins:
                if i>=coin:
                    d[i] = min(d[i],d[i-coin]+1)
        if d[amount]==(amount+1):
            return -1
        return d[amount]

"""
I think this recursive method should be correct, but maybe amount could be large and useless element
in the auxiliary array could be too many.
So maybe I should use a hashmap to just record the divisible element."""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        d = [-1]*(amount+1)
        d[0] = 0
        for coin in coins:
            if coin<amount:d[coin]=1
        #visited = [False]*(amount+1)
        coins.sort()
        print len(d)
        res = self.dp(coins,amount,d)
        if res>=1<<30:
            return -1
        else:
            return res

    def dp(self,coins,remainAmount,d):


        #if visited[remainAmount]:
        if d[remainAmount]>=0:
            return d[remainAmount]

        #visited[remainAmount]=True
        d[remainAmount]=1<<30
        #print d[remainAmount]
        for coin in coins:
            if coin<=remainAmount:
                d[remainAmount] = min(d[remainAmount],self.dp(coins,remainAmount-coin,d)+1)
            else:
                break
        return d[remainAmount]
