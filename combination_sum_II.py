#!/usr/bin/env python
# encoding: utf-8

"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
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
        if target == 0:
            if comb not in combs:
                combs.append(comb[:])
            return

        if startIndex>=len(candidates) and target>0:
            return
        elif startIndex<len(candidates) and target < candidates[startIndex]:
            return

        for i in range(startIndex,len(candidates)):
            comb.append(candidates[i])
            self.genComb(candidates,target-candidates[i],i+1,comb,combs)
            comb.pop()



"""Method2 .
Method1 is a little slow. One time consuming point is that it checks the duplicates
of comb when inserting comb to combs.
Mod is to record the previous used one and if they are duplicated, give up and continue the loop.
Be careful that it is not the same to check candidates[i]==candidates[i-1], because this will also
affect recursion. we only need to modify the loop"""
class Solution(object):
    def combinationSum2(self, candidates, target):
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
        if target == 0:
            combs.append(comb[:])
            return

        if startIndex>=len(candidates) and target>0:
            return
        elif startIndex<len(candidates) and target < candidates[startIndex]:
            return
        prev = 0
        for i in range(startIndex,len(candidates)):
            if prev==candidates[i]:
                continue
            comb.append(candidates[i])
            self.genComb(candidates,target-candidates[i],i+1,comb,combs)
            comb.pop()
            prev = candidates[i]
