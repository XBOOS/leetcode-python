#!/usr/bin/env python
# encoding: utf-8
class Solution(object):

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = list()
        for token in tokens:
            try:
                d = int(token)
                stack.append(d)
            except:
                d2 = stack.pop()
                d1 = stack.pop()
                if token == "+":
                    stack.append(d1+d2)
                elif token == "-":
                    stack.append(d1-d2)
                elif token == "*":
                    stack.append(d1*d2)
                elif token == "/":
                    stack.append(int(float(d1)/d2))
                else:
                    raise Exception("invalid operator")


        return  int(stack.pop())

