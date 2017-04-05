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

def calc_cos_sim(v1,v2):
    np_v1 = np.array(v1)
    np_v2 = np.array(v2)
    dot = np.dot(np_v1,np_v2)
    norm_v1 = np.linalg.norm(np_v1)
    norm_v2 = np.linalg.norm(np_v2)
    cos = dot/(norm_v1 * norm_v2)
    return cos


def main(matrix_file, word_raw_file):
    keyword1 = "United_States"
    keyword2 = "U.S"
    matrix,word_raw = load(matrix_file,word_raw_file)
    wv_us1 = wordvec(matrix,word_raw,keyword1)
    wv_us2 = wordvec(matrix,word_raw,keyword2)
    cos = calc_cos_sim(wv_us1,wv_us2)
    if cos is not None:
        print(cos)
    else:
        print("key={} not found".format(keyword))
    
if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
