#!/usr/bin/env python
# encoding: utf-8

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome."""
""" Method 1: using stack"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        s = [x.lower() for x in s if x.isalpha() or x.isdigit()]
        leng = len(s)
        bar = 0
        if leng%2==0:
            bar = leng/2
        else:
            bar = leng/2+1
        i = 0
        while i<leng:
            if i < leng/2:
                stack.append(s[i])
            elif i>=bar:
                tmp = stack.pop()
                if tmp!=s[i]:
                    return False
            i+=1
        return True


""" Method 2 using two pointers, still with the help of length
and did the preprocess of the list"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = [x.lower() for x in s if x.isalpha() or x.isdigit()]
        leng = len(s)
        i = 0
        while i<leng/2:
            if s[i]!=s[leng-1-i]:
                return False
            i+=1
        return True

