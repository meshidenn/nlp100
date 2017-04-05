import pickle

def ftc(t,cl,tcfreq,n):
    for c in cl:
        cs = c.strip()
        if (t,cs) in tcfreq:
            tcfreq[(t,cs)] += 1
        else:
            tcfreq[(t,cs)] = 1
        n += 1
    return n
        

def ft(t,tfreq):
    if t in tfreq:
        tfreq[t] += 1
    else:
        tfreq[t] = 1
    

def fc(cl,cfreq):
    for c in cl:
        cs = c.strip()
        if cs in cfreq:
            cfreq[cs] += 1
        elif not(cs is ''):
            cfreq[cs] = 1
    
def main():
    tcfreq = {}
    tfreq = {}
    cfreq = {}
    N = 0

    with open('context_2.txt','r') as f:
        for i, line in enumerate(f):
            wlist = line.split('\t')
            t,cl = wlist[0],wlist[1:]
            ts = t.strip()
            N = ftc(ts,cl,tcfreq,N)
            ft(ts,tfreq)
            fc(cl,cfreq)
            
    return tcfreq,tfreq,cfreq,N

if __name__ == '__main__':
    tcfreq,tfreq,cfreq,N = main()
    pickle.dump(tcfreq,open('btcfreq','wb'))
    pickle.dump(cfreq,open('bcfreq','wb'))
    pickle.dump(tfreq,open('btfreq','wb'))
    pickle.dump(N,open('bN','wb'))


#    with open('tcfreq','wb') as tc:
#        for k,v in tcfreq.items():
#            print(k,v,file=tc)
#    with open('tfreq','w') as t:
#       for k,v in tfreq.items():
#           print(k,v,file=t)
#
#   with open('cfreq','w') as c:
#       for k,v in cfreq.items():
#           print(k,v,file=c)
#
#   with open('N','w') as num:
#       print(N,file=num)
