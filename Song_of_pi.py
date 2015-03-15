# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:35:12 2015

@author: Enes kemal Ergin

Song of Pi
"""

"""
# Optional , provided by HackerRank
stripped_text = ""
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' 
for c in line:
	if c in punctuations:
		c = ""
	stripped_text += c
"""
import sys
T = int(raw_input())
pi = "31415926535897932384626433832795028841971693993751058209749445923"
while T > 0 :
    list_words = sys.stdin.readline().split()
    arr = []
    for i in list_words:
        arr.append(str(len(i)))
    
    result = ''.join(arr)
    if result == pi[:len(list_words)]:
        print("It's a pi song.")
    else:
        print("It's not a pi song.")
    T -= 1
