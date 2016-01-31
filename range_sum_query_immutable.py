#!/usr/bin/env python
# encoding: utf-8

# Bad solution to use 2-dimention array and include duplecated computation
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        leng = len(nums)
        self.chart = [[0 for _ in range(leng)] for _ in range(leng)]
        for i in xrange(leng):
            self.chart[i][i]=nums[i]

        for i in xrange(leng):
            for j in xrange(i+1,leng):
                self.chart[i][j] = self.chart[i][j-1]+nums[j]



    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.chart[i][j]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

# Method 2: one dimention
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if nums==[]:
            return None
        self.nums = nums
        self.sums = [0]*len(nums)
        self.sums[0] = nums[0]
        for i in range(1,len(nums)):
            self.sums[i] = self.sums[i-1]+nums[i]


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j]-self.sums[i]+self.nums[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
