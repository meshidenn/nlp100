# coding: utf-8

import sys

c = 'パトカー'
d = 'タクシー'
lc = len(c)
ld = len(d)
rev = ''
for i in range(0,ld):
    rev += c[i]
    rev += d[i]
    print(i)
print(rev)





