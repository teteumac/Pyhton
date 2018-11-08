# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:26:54 2018

@author: mathe
"""


def counter(n):
    count = 0
    while n!=0:
        if n % 10 == 5 or n % 10==0:
            count=count + 1
        n = n//10

    return count

v=counter(20051)

print(v)
