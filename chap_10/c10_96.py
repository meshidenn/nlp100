# -*- coding utf-8 -*-

from gensim.models import word2vec
import sys
import pickle

def main(model_file, nation_file, out_file):
    nations = []
    with open(nation_file,'r') as f:
        for line in f:
            nations.append(line.strip())

    model = word2vec.Word2Vec.load(model_file)

    vms = {}

    for n in nations:
        vms[n] = model.wv[n]

    pickle.dump(vms, open(out_file,'wb'))

if __name__ == '__main__':
    argvs = sys.argv
    model_file = argvs[1]
    nation_file = argvs[2]
    out_file = argvs[3]
    main(model_file, nation_file, out_file)


