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
    if norm_v1 != 0 and norm_v2 != 0:
        cos = dot/(norm_v1 * norm_v2)
    else:
        cos = 0.0
    return cos

def get_sim_words(mat, base, raw_word_file, cut = 10):
    rank = []
    sim_words = []
    for v in mat:
        if all([i == j for i, j in zip(base,v)]):
               continue
        cos = calc_cos_sim(base,v)
        rank.append(cos)
    np_rank = np.array(rank)
    srank = np.sort(np_rank)[::-1]
    arank = np.argsort(np_rank)[::-1]
    print(srank[0:10])
    print(arank[0:10])

    index_words = arank[0:cut]

    with open(raw_word_file,'rb') as wr:
        raw_word = pickle.load(wr)

    for i in index_words:
        w = raw_word[i]
        sim_words.append(w)

    return sim_words


def main(matrix_file, word_raw_file, raw_word_file):
    keyword1 = "England"
    matrix,word_raw = load(matrix_file,word_raw_file)
    wv_uk = wordvec(matrix,word_raw,keyword1)
    sim_words = get_sim_words(matrix,wv_uk,raw_word_file)

    return sim_words

    
    
if __name__ == '__main__':
    sim_words = main(sys.argv[1],sys.argv[2],sys.argv[3])
    print(sim_words)
