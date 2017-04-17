# -*- coding utf-8 -*-

import numpy as np
import scipy as sp
import pandas as pd
import sys

def cor_spi(rank1,rank2):
    n = len(rank1)
    dif = 0.0
    for k,v in rank1.items():
        tmp = (rank1[k] - rank2[k]) ** 2
        dif += tmp
    cor = 1 - 6.0/(float((n*(n**2-1.0))))*dif
    return cor
                              

def main(infile,outfile):
    sim1 = {}
    sim2 = {}
    sim3 = {}
    with open(infile,'r') as f:
        for line in f:
            tmp = line.strip().split(',')
            sim1[tmp[0],tmp[1]] = float(tmp[2])
            sim2[tmp[0],tmp[1]] = float(tmp[3])
            sim3[tmp[0],tmp[1]] = float(tmp[4])

    rank_hum = {}
    rank_pca = {}
    rank_w2v = {}

    for rank, (k,v) in enumerate(sorted(sim1.items(), key=lambda x: -x[1])):
        rank_hum[k] = rank + 1

    for rank, (k,v) in enumerate(sorted(sim2.items(), key=lambda x: -x[1])):
        rank_pca[k] = rank + 1

    for rank, (k,v) in enumerate(sorted(sim3.items(), key=lambda x: -x[1])):
        rank_w2v[k] = rank + 1

    print(rank_hum)
    print(rank_pca)
    print(rank_w2v)
    cor1 = cor_spi(rank_hum,rank_pca)
    cor2 = cor_spi(rank_hum,rank_w2v)
    cor3 = cor_spi(rank_pca,rank_w2v)

    with open(outfile,'w') as g:
        print(cor1,cor2,cor3,file=g)

if __name__ == '__main__':
    argvs = sys.argv
    infile = argvs[1]
    outfile = argvs[2]
    main(infile, outfile)

