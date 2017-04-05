import pickle
import sys
import numpy as np
import scipy as sp
from scipy import io, sparse


def load(matrix_file,word_raw_file):
    matrix = io.loadmat(matrix_file)['pca_300']
    with open(word_raw_file,'rb') as wr:
        word_raw = pickle.load(wr)

    return matrix, word_raw

    

def wordvec(matrix,word_raw,keyword):
    index = word_raw.get(keyword,None)
    if index is not None:
        return matrix[index]
    else:
        return None
    

def main(matrix_file, word_raw_file):
    keyword = "United_States"
    matrix,word_raw = load(matrix_file,word_raw_file)
    print(word_raw[keyword])
    print(matrix)
    wv = wordvec(matrix,word_raw,keyword)
    if wv is not None:
        print(wv)
    else:
        print("key={} not found".format(keyword))
    
if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
