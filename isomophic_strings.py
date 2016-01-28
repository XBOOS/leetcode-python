#!/usr/bin/env python
# encoding: utf-8

"""

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            ss = s[i]
            if not ss in s_dict:
                s_dict[ss] = [i]
            else:
                s_dict[ss].append(i)
        for j in range(len(t)):
            tt = t[j]
            if not tt in t_dict:
                t_dict[tt] = [j]
            else:
                t_dict[tt].append(j)

        return sorted(s_dict.values())==sorted(t_dict.values())
