def coln(fname):
    f = open(fname,'r')
    l = 0
    for line in f:
        l += 1

    f.close()
    return l


import sys

args = sys.argv

#the number of col in file 
row = coln(args[1])

#the input of dividing number
n = int(args[2])

dev = row/n
res = row - dev * n

# set index num
i = 0
j = 1
k = 1
cnt = j * dev
name = 'div{0}'.format(k)
print(name)
f = open(args[1],'r')
g = open(name,'w')

for line in f:
    i += 1
    g.write(line)
    if i == cnt and i < row:
        g.close()
        j += 1
        cnt = j * dev
        k += 1
        name = 'div{0}'.format(k)
        print(name)
        g = open(name,'w')
    elif i == row:
        g.close()

f.close
