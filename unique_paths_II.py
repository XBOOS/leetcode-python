#!/usr/bin/env python
# encoding: utf-8

"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2."""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0]*n for _ in range(m)]
        ii = jj = 0
        while ii<n:
            if obstacleGrid[0][ii]==0:
                dp[0][ii]=1
                ii+=1
            else:
                break
        while jj<m:
            if obstacleGrid[jj][0]==0:
                dp[jj][0]=1
                jj+=1
            else:
                break

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1] if obstacleGrid[i][j]==0 else 0
        return dp[-1][-1]
