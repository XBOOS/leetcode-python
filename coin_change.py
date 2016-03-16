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
Still not right.remain to be changed"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        mins = [float('inf')]*(amount+1)
        mins[0]=0
        for i in range(1,amount+1):
            for j in range(1,len(coins)):
                if i>=coins[j]:
                    mins[i] = min(mins[i],mins[i-coins[j]]+1)

        return mins[amount]



class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        d = [-1]*(amount+1)
        #visited = [False]*(amount+1)
        coins.sort()
        res = self.dp(coins,amount,d)
        if res==(1<<30):
            return -1
        else:
            return res

    def dp(self,coins,remainAmount,d):

        if remainAmount<=0:
            return 0
        #if visited[remainAmount]:
        if d[remainAmount]>=0:
            return d[remainAmount]

        #visited[remainAmount]=True
        d[remainAmount]=1<<30
        for coin in coins:
            if coin<=remainAmount:
                d[remainAmount] = min(d[remainAmount],self.dp(coins,remainAmount-coin,d)+1
        return d[remainAmount]
