#!/usr/bin/env python
# encoding: utf-8
"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"]."""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        helper1 = set()
        helper2 = set()
        res = list()
        for i in range(n-9):
            seq = s[i:i+10]
            if seq in helper1 and seq not in helper2:
                res.append(seq)
                helper2.add(seq)
                continue
            helper1.add(seq)
        return res

""" Method2 this is with a tag of Bit Manipulation.
instead of 0/1 there are ACGT four different types of bit. so it need 2 binry bit.
and each shifting is <<2. Can use a hashmap( ACGT=> 0,1,2,3) and the binary representation
as the key to do the hash. How fast it helps? """




