#/usr/bin/env python

#Multiples of 3 or 5

def solution(number):
    summary = 0
    for i in range(number):
        if i % 3 == 0:
            summary += i
        elif i % 5 == 0:
            summary += i
    return summary
