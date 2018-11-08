# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:29:33 2018

@author: mathe
"""

def collatz(n):
    print(n)
    if n == 1:
        return n
    if n % 2 == 0:
        collatz(n / 2)
    else:
        collatz(3 * n + 1)

collatz(3)
