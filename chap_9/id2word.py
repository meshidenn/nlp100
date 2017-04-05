import pickle
from collections import defaultdict


def main():
    w2raw = defaultdict(None)
    cow2col = defaultdict(None)
    
    with open('raw_word_2','rb') as word:
        raw2w = pickle.load(word)
#        a = pickle.load(word)
        print(raw2w)
#        print(a)

    with open('col_coword','rb') as coword:
        col2cw = pickle.load(coword)
#        print(col2cw)

    for i in range(len(raw2w)):
        w2raw[raw2w[i]] = i

    for i in range(len(col2cw)):
        cow2col[col2cw[i]] = i 

    pickle.dump(w2raw,open('word_raw','wb'))
    pickle.dump(cow2col,open('coword_col','wb'))



if __name__ == "__main__":
    main()
