import pickle
from collections import defaultdict

w2r = defaultdict(None)

with open('btfreq','rb') as t:
    tfreq = pickle.load(t)

for i,w in enumerate(tfreq):
    w2r[w] = i

pickle.dump(w2r,open('word_raw_2','wb'))
        
        
