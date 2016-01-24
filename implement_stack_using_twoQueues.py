#!/usr/bin/env python
# encoding: utf-8

class Stack(object):
    class Queue(object):
        def __init__(self):
            self.queue = list()
        def push(self,x):
            self.queue.append(x)
        def peek(self):
            if self.empty():
                raise Exception("Empty queue!")
            return self.queue[0]
        def pop(self):
            res = self.peek()
            del self.queue[0]
            return res
        def size(self):
            return len(self.queue)
        def empty(self):
            return self.size()==0


    def __init__(self):
        """
        initialize your data structure here.
        """
        self.current = self.Queue() #toPush = True
        self.backup = self.Queue() #toPop = True


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.current.push(x)


    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty():
            raise Exception("Empty Stack!")

        while self.current.size()>1:
            self.backup.push(self.current.pop())
        res = self.current.pop()
        self.current,self.backup = self.backup,self.current
        return res



    def top(self):
        """
        :rtype: int
        """
        if self.empty():
            raise Exception("Empty Stack!")

        while self.current.size()>1:
            self.backup.push(self.current.pop())
        res = self.current.peek()
        self.backup.push(self.current.pop())
        self.current,self.backup = self.backup,self.current
        return res


    def empty(self):
        """
        :rtype: bool
        """
        return self.current.empty() and self.backup.empty()

