f = open('hightemp.txt','r')
g = open('col1.txt','w')
h = open('col2.txt','w')

col1 = []
col2 = []

for line in f:
    buf = line.split('\t')
    g.write(buf[0]+'\n')
    h.write(buf[1]+'\n')

f.close
g.close
h.close
