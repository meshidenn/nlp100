import nltk
import re
from collections import Counter

pattern = u'''(?x) ([A-Z]\.)+ | \w+(-\w+)* | \$?\d+(\.\d+)?%? | [][.,;"'?():-_`] '''
porter = nltk.PorterStemmer()

wlist = []
wlist2 = []

with open('sentiment.txt','r') as f:
    for line in f:
        l = re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*",line)
        l2 = nltk.word_tokenize(line)
        wlist += l
        wlist2 += l2
        
#    print(wlist)
print(wlist2)


stem = [porter.stem(t) for t in wlist2]
tagger = nltk.pos_tag(stem)
dtagger = dict(tagger)
#print(dtagger)
fdist = nltk.FreqDist(wlist)
counter = Counter(wlist)

#for word, count in counter.most_common():
#    print(word.strip())
    
#for word in fdist:
#    print(word,':',fdist[word])
        
        
