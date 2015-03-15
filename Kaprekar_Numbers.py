# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 17:16:00 2015

@author: Enes kemal Ergin

Kaprekar Numbers
"""
def kaprekar_numbers(x):
	l = str(x*x)
	return x == int(l[:len(l)/2] or 0) + int(l[len(l)/2:])

list_kaprekar = [str(x) for x in xrange(int(raw_input()), int(raw_input())+1) if kaprekar_numbers(x)]
if len(list_kaprekar) != 0:
    print(" ".join(list_kaprekar))
else:
    print("INVALID RANGE")

