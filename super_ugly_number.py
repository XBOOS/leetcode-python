#!/usr/bin/env python
# encoding: utf-8

"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000."""


""" Method1 using the heapq, with time complexity of O(kn) but TLE"""
import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = len(primes)
        heap = [1]
        count = 1
        while count<n:
            smallest = heapq.heappop(heap)
            for i in primes:
                if smallest*i not in heap:
                    heapq.heappush(heap,smallest*i)
            count+=1
        return heapq.heappop(heap)
