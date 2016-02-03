#!/usr/bin/env python
# encoding: utf-8
import time
"""
to decide whether two chars have common characters,
can use bit manipulation and set
To compare the speed here"""
A = "asdfasgrtherthasdfasgafdgasdfasdg"*100
B = "iojoeirjgoijoprthkdfnbknskfbnksdlfbklsfdkbsdfb"*100


bag1= set()
bag2 = set()
start = time.time()
for s in A:
    bag1.add(s)
cm =0
for s in B:
    if s in bag1:
        cm =1
    bag2.add(s)
end = time.time()
print "Using set used time ",end-start, "  the result is ",cm==1

# bit manipulation
value1 = value2 = 0
start = time.time()
for s in A:
    value1 |=1<<(ord(s)-ord('a'))
for s in B:
    value2 |=1<<(ord(s)-ord('a'))
end = time.time()
print "Using bits used time ",end-start, "  the result is ",(value1&value2)!=0

