def tail(fname,n,l):
    f = open(fname,'r')
    w = []
    i = 0
    for line in f:
        i += 1
        if i <= l-n:
            continue
        w.append(line) 

    f.close()
    return w

def coln(fname):
    f = open(fname,'r')
    l = 0
    for line in f:
        l += 1

    f.close()
    return l



import sys

args = sys.argv

num = coln(args[1])
print(num)
res = tail(args[1],int(args[2]),num)

for i in range(0,int(args[2])):
    print(res[i],end='')
