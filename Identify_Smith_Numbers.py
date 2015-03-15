# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 00:41:30 2015

@author: Enes Kemal Ergin

Identify Smith Numbers
"""
import math
def FindFactors(number):
    factors = []
    while(number % 2 == 0):
        factors.append(2)
        number = number / 2
    #End While
    #Looking for Odd factors
    i = 3
    max_factor = math.sqrt(number)
    while(i <= max_factor):
        while((number % i) == 0):
            # i is a factor add the list
            factors.append(i)        
            # divide the number by i
            number = number / i
            # set a new upper bond
            max_factor = math.sqrt(number)
        # End While
        # Checks next ODD number
        i = i + 2
    # End While
    
    if (number > 1):
        factors.append(number)
    return factors

def sumthem(a, sum = 0):
    while a:
        sum += a % 10
        a //= 10
    return sum

N = int(raw_input())

sum_numbers = sumthem(N)

factorList = FindFactors(N)
sum_factors = 0
for i in factorList:
    sum_factors = sumthem(i, sum_factors)
if sum_numbers == sum_factors:
    print 1
else:
    print 0