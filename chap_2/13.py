f = open('col1.txt','r')
g = open('col2.txt','r')
h = open('comb.txt','w')

c = []
d = []
l = 0

for line in f:
    c.append(line)
    l += 1

for line in g:
    d.append(line)

for i in range(0,l):
    w = c[i].rstrip('\n') + '\t' + d[i]
    h.write(w)

f.close
g.close
h.close
