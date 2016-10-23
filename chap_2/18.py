import sys
from operator import itemgetter,attrgetter

args = sys.argv

f = open(args[1],'r')
cont = []

for line in f:
    buf = line.split('\t')
    cont.append(buf)

res = sorted(cont, key=itemgetter(2),reverse=True)
print(res)
f.close

