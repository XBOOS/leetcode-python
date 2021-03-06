#!/usr/bin/env python
# encoding: utf-8

"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1]."""


""" Method 1: Insertion"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        leng = len(nums)
        if leng==0:
            return []
        perms = [[nums[0]]]
        for i in range(1,leng):
            n = len(perms) # must be careful, record the original length in advance instead of changing length
            for j in range(n):
                for k in range(i):
                    newPerm = perms[j][:]
                    newPerm.insert(k,nums[i])
                    perms.append(newPerm)
                perms[j].append(nums[i])
        return perms


""" Method 2: using backtracking. Recursion + maintain [used] to prune the used num"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        leng = len(nums)
        perm = []
        perms = []
        used = [False]*leng
        self.genPerms(nums,used,perms,perm)
        return perms

    def genPerms(self,nums,used,perms,perm):
        if len(perm)==len(nums):
            perms.append(perm[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            perm.append(nums[i])
            used[i] = True
            self.genPerms(nums,used,perms,perm)
            perm.pop()
            used[i] = False

