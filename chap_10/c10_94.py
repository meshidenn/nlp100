
# -*- coding: utf-8 -*-

from gensim.models import word2vec
import logging
import sys
import pickle
import numpy as np
import scipy as sp
from scipy import io, sparse

def load_mat(matrix_file, word_raw_file):
    matrix = io.loadmat(matrix_file)['pca_300']
    with open(word_raw_file,'rb') as wr:
        word_raw = pickle.load(wr)

    return matrix, word_raw

def wv_sim(matrix, word_raw, word1, word2):
    index1 = word_raw.get(word1,None)
    index2 = word_raw.get(word2,None)
    if index1 is not None:
        wv1 = matrix[index1]
    else:
        sim = np.nan
        return sim

    if index2 is not None:
        wv2 = matrix[index2]
    else:
       sim = np.nan
       return sim

    wv1l = np.linalg.norm(wv1)
    wv2l = np.linalg.norm(wv2)
    sim = np.dot(wv1,wv2)/(wv1l*wv2l)
    return sim

def load_w2v(w2vfile):
    model = word2vec.Word2Vec.load(w2vfile)
    return model

def w2v_sim(model,word1, word2):
    try:
        sim = model.wv.similarity(word1, word2)
    except:
        sim = np.nan
    return sim


def main(in_file, out_file, matrix_file, word_raw_file, w2vfile):
    matrix,word_raw = load_mat(matrix_file, word_raw_file)
    model = load_w2v(w2vfile)
    with open(in_file,'r') as f:
        if '.csv' in in_file:
            delim = ','
        elif '.tsv' in in_file:
            delim = '\t'
            
        for i,line in enumerate(f):
            if i == 0:
                continue
            tmp = line.strip().split(delim)
            word1, word2, sim0 = tmp[0], tmp[1], tmp[2]
            print(word1,word2,sim0)
            s1 = wv_sim(matrix,word_raw,word1,word2)
            s2 = w2v_sim(model, word1, word2)
            sim1 = s1 * 10.0
            sim2 = s2 * 10.0
            print('{},{},{},{},{}'.format(word1,word2,sim0,sim1,sim2))
            if i == 1:
                with open(out_file,'w') as g:
                    print('{},{},{},{},{}'\
                          .format(word1,word2,sim0,sim1,sim2),  file=g)
            else:
                with open(out_file,'a') as g:
                    print('{},{},{},{},{}'\
                          .format(word1,word2,sim0,sim1,sim2),  file=g)
    

if __name__ == '__main__':
    argvs = sys.argv
    main(argvs[1],argvs[2],argvs[3],argvs[4],argvs[5])
