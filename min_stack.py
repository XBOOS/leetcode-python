#!/usr/bin/env python
# encoding: utf-8

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

"""Need to maintain another piece of information, also could make 2 list associate, like list of nodes(having two fileds)"""
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.minstack = list()
        self.minstack.append(2**31-1)
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        self.minstack.append(min(self.minstack[-1],x))


    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]

