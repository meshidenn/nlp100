import numpy as np
import scipy as sp
import pickle
from collections import defaultdict
from scipy import io, sparse

def ppmi_matrix(tcfreq,tfreq,cfreq,N,threshold=10):
    tlen = len(tfreq)
    clen = len(cfreq)
    matrix = sparse.lil_matrix((tlen,clen))
    raw2w = defaultdict(None)
    col2cow = defaultdict(None)

    for i, t in enumerate(tfreq):
        raw2w[i] = t
        print(i,t)
        for j, c in enumerate(cfreq):
            if i == 0:
                col2cow[j] = c
            if (t,c) in tcfreq:
                if tcfreq[(t, c)] >= threshold:
                    print((t, c), tcfreq[(t, c)])
                    pmi = np.log(N) + np.log(tcfreq[(t,c)]) \
                          - np.log(tfreq[t]) - np.log(cfreq[c])
                    matrix[i,j] = max(pmi,0)

    return raw2w ,col2cow ,matrix
   

def main():
    tcfreq = {}
    tfreq = {}
    cfreq = {}
    
    with open('btcfreq','rb') as tc:
        tcfreq = pickle.load(tc)
      
    with open('btfreq','rb') as t:
        tfreq = pickle.load(t)
           

    with open('bcfreq','rb') as c:
        cfreq = pickle.load(c)

    with open('bN','rb') as N:
        N = pickle.load(N)

    raw2w,col2cow,matrix = ppmi_matrix(tcfreq,tfreq,cfreq,N)
    io.savemat('ppmi_matrix',{"ppmi":matrix})
    pickle.dump(raw2w,open('raw_word','wb'))
    pickle.dump(col2cow,open('col_coword','wb'))


if __name__ == "__main__":
    main()

    
