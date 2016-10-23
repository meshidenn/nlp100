def ngram(char,n):
    gram = []
    l = len(char)
    for i in range(0,l-n+1):
        buf = ''
        for j in range(i,n+i):
            buf += char[j]
        gram.append(buf)

    return gram

import sys

args = sys.argv
col1 = []
num_w = []

f = open(args[1],'r')
i = 0

for line in f:
    buf = line.split('\t')
    col1.append(buf[0])
    num_w.append(len(buf[0]))
    i += 1

n = max(num_w)
sort = set()

for j in range(0,i):
    for k in range(0,n):
       buf = ngram(col1[j],k)
       sort = sort.union(set(buf))
    
print(sort)
