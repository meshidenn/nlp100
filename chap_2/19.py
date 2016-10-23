import sys

args = sys.argv
f = open(args[1],'r')
mid = []
row = 0

for line in f:
    buf = line.split('\t')
    mid.append(buf[0])

mid.sort()
print(mid)
count = 1
freq = {}
row = len(mid)
lim = row - 1

for i in range(0,row):
    if (i < lim) and (mid[i] == mid[i+1]):
        count += 1
    else:
        freq[mid[i]] = count
        count = 1

for k,v in sorted(freq.items(),key=lambda x:x[1],reverse=True):
    print(k,v)


        
