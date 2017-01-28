# -*- coding: utf-8 -*-

out = open('sentiment.txt','w')
with open('/Users/hiroki/program/python/nlp100/chap_8/rt-polaritydata/rt-polaritydata/rt-polarity.pos','r',encoding = "ISO-8859-1") as f:
    for line in f:
        print('success')
        lbline = u"+1 " + line
        print(lbline,file=out,end='')

with open('/Users/hiroki/program/python/nlp100/chap_8/rt-polaritydata/rt-polaritydata/rt-polarity.neg','r',encoding = "ISO-8859-1") as g:
    for line in g:
        lbline= u"-1 " + line
        print(lbline,file=out,end='')

out.close()
