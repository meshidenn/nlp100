#!/usr/bin/env python
# coding: utf-8

import MeCab
from collectiond import OrderedDict

mecab = MeCab.Tagger("-Ochasen /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
mecab.parse('')
f = open('neko.txt','r')

doc = []


for line in f:
    node = mecab.parseToNode(line)
    sent = OrderedDict()
    while node:
        word = node.surface
        base = node.feature.split(",")[6]
        pos = node.feature.split(",")[0]
        pos1 = node.feature.split(",")[1]
        sent['surface'] = word
        sent['base'] = base
        sent['pos'] = pos
        sent['pos1'] = pos1
#        print('{0},{1},{2},{3}'.format(word,base,pos,pos1))
        node = node.next
        

f.close()
    
    
