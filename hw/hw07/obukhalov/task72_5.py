#/usr/bin/env python

#Reversing Words in a String

def reverse(st):
    l = list(st.split())
    l.reverse()
    st = " ".join(l)
    return st
