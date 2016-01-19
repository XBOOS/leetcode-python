#!/usr/bin/env python
# encoding: utf-8

"""Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue)."""
class Queue(object):
    #inner stack class
    class Stack(object):
        def __init__(self):
            self.stack = list()
        def push(self,x):
            self.stack.append(x)
        def pop(self):
            if len(self.stack)<1:
                raise Exception("Empty stack")
            return self.stack.pop()
        def peek(self):
            if len(self.stack)<1:
                raise Exception("Empty stack")
            return self.stack[len(self.stack)-1]

        def size(self):
            return len(self.stack)
        def empty(self):
            return len(self.stack)==0

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = self.Stack()
        self.stack2 = self.Stack()
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.stack2.empty():
            self.stack1.push(x)
        else:
            while not self.stack2.empty():
                self.stack1.push(self.stack2.pop())
            self.stack1.push(x)


    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty():
            raise Exception("Empty Queue")
        elif self.stack1.empty() and not self.stack2.empty():
            self.stack2.pop()
        else:
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
            self.stack2.pop()


    def peek(self):
        """
        :rtype: int
        """
        if self.empty():
            raise Exception("Empty Queue")
        elif self.stack1.empty() and not self.stack2.empty():
            return self.stack2.peek()
        else:
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
            return self.stack2.peek()


    def empty(self):
        """
        :rtype: bool
        """
        return self.stack1.empty() and self.stack2.empty()
