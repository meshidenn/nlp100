from collections import OrderedDict

f = open('neko.txt.mecab','r')
g = open('map.txt','w')
sent=[]
d = OrderedDict()


for line in f:
    if line == 'EOS\n':
        print(sent)
        sent = []
        continue

    suf = line.split('\t')[0]
    feature = line.split('\t')[1]
    pos = feature.split(',')[0]
    pos1 = feature.split(',')[1]
    base = feature.split(',')[6]
    d['surface'] = suf
    d['base'] = base
    d['pos'] = pos
    d['pos1'] = pos1
    sent.append([(k,v) for (k,v) in d.items()])

f.close()
g.close()
