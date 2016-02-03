#!/usr/bin/env python
# encoding: utf-8

"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.

"""
"""
The intuition is to use sets to detect duplicates and common characters,
but this solution exceeds time limit"""
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words or len(words)<2:
            return 0
        sets = [set() for _ in range(len(words))]

        product = 0
        for i in range(len(words)):
            word = words[i]
            for ii in range(i):
                j=0
                while j< len(word):
                    if word[j] in sets[ii]:
                        break
                    j+=1
                if j==len(word):
                    product = max(product,len(words[ii])*len(word))
                #put chars of new words into set
            for ss in word:
                sets[i].add(ss)
        return product

"""Method 2 using bit manipulation, 1 on specific bit represents one specific character
then use & to detect common characters, faster then one pass to detect from the set"""
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        leng = len(words)
        if leng<2:
            return 0
        product = 0
        value = [0 for _ in range(leng)]
        for i in range(leng):
            for ss in words[i]:
                value[i] |= (1<<(ord(ss)-65))
        for i in range(leng):
            for j in range(i,leng):
                if value[i]&value[j]==0:
                    product = max(product,len(words[i])*len(words[j]))
        return product

""" records the length of the words, use more space to make it even faster"""
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        leng = len(words)
        if leng<2:
            return 0
        product = 0
        lengs = [0 for _ in range(leng)]
        value = [0 for _ in range(leng)]
        for i in range(leng):
            lengs[i] = len(words[i])
            for ss in words[i]:
                value[i] |= (1<<(ord(ss)-65))
        for i in range(leng):
            for j in range(i,leng):
                if value[i]&value[j]==0:
                    product = max(product,lengs[i]*lengs[j])
        return product


