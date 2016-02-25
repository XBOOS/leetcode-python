#!/usr/bin/env python
# encoding: utf-8

"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
"""

"""
Using backtracking: a general method to find all(or some)solutions to the problem.
Based on brute force, it also incrementally builds candidates to the solution,until
and abandons each partial candidate (backtracks) as soon as it determines
that this candidate cannot be possibly completed to a valid solution

The key point is
1. the recursion : recursive call
2. the base case== also the ending rules(where i found the valid solution or where i should backtrack)"""

"""
Another I should remember is that I should append the copy of comb( list is just shallow copy of pointer)"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        comb = []
        combs = []
        self.genComb(candidates,target,0,comb,combs)
        return combs
    def genComb(self,candidates,target,startIndex,comb,combs):
        if startIndex<len(candidates):
            if target == 0:
                combs.append(comb[:])
                return
            elif target<candidates[startIndex]:
                return
        else:
            if target>0:
                return

        for i in range(startIndex,len(candidates)):
            comb.append(candidates[i])
            self.genComb(candidates,target-candidates[i],i,comb,combs)
            comb.pop()


""" Method2. slightly modified the ending check rule to make code simple.
But it also deepens the recrusion stack and make it much slower"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        comb = []
        combs = []
        self.genComb(candidates,target,0,comb,combs)
        return combs
    def genComb(self,candidates,target,startIndex,comb,combs):
        if target<0:
            return
        elif target==0:
            combs.append(comb[:])
            return

        for i in range(startIndex,len(candidates)):
            comb.append(candidates[i])
            self.genComb(candidates,target-candidates[i],i,comb,combs)
            comb.pop()

