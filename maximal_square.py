#!/usr/bin/env python
# encoding: utf-8
"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.

"""
""" Method1 Dynamic programming.
The transformation equation is not easy to come up with"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix==[]:return 0
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 if matrix[i][j]=='0' else 1 for j in xrange(n)]for i in xrange(m)]
        maxEdge = max(max(dp[0]),max([row[0] for row in dp]))
        for i in range(1,m):
            for j in range(1,n):
                if dp[i][j]==1:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    maxEdge = max(maxEdge,dp[i][j])
        return maxEdge**2

""" Clever modify in the loop enter condition to simply the maxEdge initialization. The different looping process could be combined"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix==[]:return 0
        m = len(matrix)
        n = len(matrix[0])
        maxEdge = 0
        dp = [[0]*(n) for _ in xrange(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j])
                if i and j and dp[i][j]:
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
                maxEdge = max(maxEdge,dp[i][j])

        return maxEdge*maxEdge


""" Brute force : Time limit exceeded!!"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix==[]:return 0
        m = len(matrix)
        n = len(matrix[0])

        #Method1 : brute force
        def valid(i,j,k):
            for ii in range(i,k+1):
                for jj in range(j,j+(k+1-i)):
                    if matrix[ii][jj]==0:return False
            return True
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='0':continue
                for k in range(i,m):
                    if j+k-i<n and valid(i,j,k):
                        maxArea = max(maxArea,(m-i+1)*(m-i+1))
        return maxArea



""" Method 3 O(mnn), slower but provide a different sight view"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix==[]:return 0
        m = len(matrix)
        n = len(matrix[0])
        colSum = [1 if x=="1" else 0 for x in matrix[0]]
        maxArea = max(colSum)
        for i in range(1,m):
            for j in range(n):
                if matrix[i][j]=="1":
                    colSum[j] +=1
                else:
                    colSum[j] = 0

            for j in range(n):
                minH = colSum[j]
                for k in range(j,n):
                    if colSum[k]==0:break
                    minH = min(colSum[k],minH)
                    maxArea = max(maxArea,min(minH,(k-j+1))**2)


        return maxArea

