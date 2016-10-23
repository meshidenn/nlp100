f = open('hightemp.txt','r')
g = open('11.txt','w')

for line in f:
    rep = line.expandtabs(1)
    g.write(rep)

f.close
g.close
