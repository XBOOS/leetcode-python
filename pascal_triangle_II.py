#!/usr/bin/env python
# encoding: utf-8

"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1]."""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #maintain two levels

        row = 1
        previous = [1,1]
        current = [1]
        if rowIndex < 0:
            return []
        elif rowIndex == 0:
            return [1]
        else:
            while row < rowIndex+1:
                for k in range(1,row):
                    current.append(previous[k-1]+previous[k])
                current.append(1)
                row += 1
                previous = current[:]
                current = [1]
            return previous

"""Method 2 using the property of the coefficient of the items in the C(n,k) = C(n,k-1)*(n-k+1)/k"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #maintain two levels

        if rowIndex <0:
            return []
        elif rowIndex == 0:
            return [1]

        result = [1]*(rowIndex+1)
        for i in range(1,(1+rowIndex)/2+1):
            result[i] = result[rowIndex-i] = result[i-1]*(rowIndex+1-i)/i

        return result


"""Method 3 this uses one array to store the items and update it by loop. Very smart solution from others!!! I appreciate it"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #maintain two levels

        if rowIndex <0:
            return []
        n = rowIndex
        result = [0]*(2*n+3)
        left = right = n+1
        result[left]=1
        n -= 1
        while n>=0:
            left -=1
            right +=1
            i = left
            while i <= right:
                result[i] = result[i-1]+result[i+1]
                i +=2
            n -= 1
        print result
        return result[left::2]






