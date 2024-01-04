#/usr/bin/env python

#Counting sheep

def count_sheeps(sheep):
    return len(list(filter(lambda x: x == True, sheep)))
