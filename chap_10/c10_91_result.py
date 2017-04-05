# -*- coding: utf-8 -*-

from gensim.models import word2vec
import logging
import sys

model = word2vec.Word2Vec.load("sample.model")


def p85(word):
    vm = model.wv[word]
    print(word,' ',vm)

def p86(word1,word2):
    sim = model.wv.similarity(word1, word2)
    print(word1,' ',word2,' ',sim)


def s(posi, nega=[], n=10):
    cnt = 1
    result = model.wv.most_similar(positive = posi, negative = nega, topn = n)
    for r in result:
        print(cnt,' ',r[0],' ',r[1])
        cnt += 1

if __name__ == '__main__':
#    word = sys.argv[1]
#    word = str(word)
    p85("United_States")
    print("United States Similality")
    p86("United_States","U.S")
    print("England Similality")
    s("England")
    print("Spain - Madrid + Athnes")
    s(["Spain","Athens"],["Madrid"])
