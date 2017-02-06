import re

cap = re.compile('[A-Z,a-z]')
nl = []

with open('raw_nation.txt','r') as f:
    for line in f:
        buf = []
        buf_uniq = []
        wl = line.split()
        for i in range(1,len(wl)):
            t = cap.match(wl[i])
            s = cap.match(wl[i-1])
            if t and (not s):
                buf.append(wl[i])
            elif t and s:
                buf.append(wl[i-1])
                buf.append(wl[i])
        for x in buf:
            if x not in buf_uniq:
                buf_uniq.append(x)

#        print(buf_uniq)

        w = ' '.join(buf_uniq)
        nl.append(w)
        

snl = sorted(nl)

for sn in snl:
    print(sn)


        
