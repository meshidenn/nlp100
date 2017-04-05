#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
quoting from chanreta
"""

"""
83. 単語／文脈の頻度の計測
82の出力を利用し，以下の出現分布，および定数を求めよ．
・f(t,c): 単語tと文脈語cの共起回数
・f(t,∗): 単語tの出現回数
・f(∗,c): 文脈語cの出現回数
・N: 単語と文脈語のペアの総出現回数
"""

from collections import defaultdict
import sys
import pickle


class Context:

    def __init__(self, doc):
        self.doc = doc
        co_occ = defaultdict(int)
        t_occ = defaultdict(int)
        c_occ = defaultdict(int)
        N = 0

        for line in doc:
            words = line.strip().split("\t")
            t = words[0]
            t_occ[t] += 1
            for c in words[1:]:
                c_occ[c] += 1
                co_occ[(t, c)] += 1
                N += 1
        self.co_occ = co_occ
        self.t_occ = t_occ
        self.c_occ = c_occ
        self.N = N


def main(in_file, out_file):
    context = None
    with open(in_file) as f:
        context = Context(f.readlines())
    pickle.dump(context, open(out_file, 'wb'))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
