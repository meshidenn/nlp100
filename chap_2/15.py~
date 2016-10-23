def head(fname,n):
    f = open(fname,'r')
    i = 0
    w = []
    for line in f:
        i += 1
        w.append(line) 
        if i >= n:
            break

    f.close()
    return w

import sys

args = sys.argv

res = head(args[1],int(args[2]))

for i in range(0,int(args[2])):
    print(res[i],end='')
