import sklearn as skl
from sklearn.linear_model import LogisticRegression
import numpy as np
import nltk

def mkwpdict(swlist,file):
    porter = nltk.PorterStemmer()
    wpdict = {}
    for line in file:
         sep = line.strip().split(':')
         key = porter.stem(sep[0])
         val = sep[1:]
         if not(key in swlist):
             wpdict[key] = val
    return wpdict

def makexy(wpdict,file):
    porter = nltk.PorterStemmer()
    x = []
    y = []
    wlist = []
    wwlist = []
    for line in file:
        tokens = nltk.word_tokenize(line)
        point = int(tokens[0])
        stem =[porter.stem(t) for t in tokens[1:]]
        wlist += stem
        wwlist.append(stem)
        y.append(point)
    wset = set(wlist)
    slist = sorted(list(wset))
    n = len(slist)
    for stems in wwlist:
        points = np.zeros(n)
        for w in stems:
            if w in wpdict:
               i = slist.index(w)
#               print(w,wpdict[w][1])
               points[i] += float(wpdict[w][1])

        x.append(points)

#    print(x)
#    print(y)
    return x,y,slist
               
def learning(x,y):
    x_np = np.array(x)
    y_np = np.array(y)
                
    lr = LogisticRegression()
    lr.fit(x,y)

    return lr

def main():
    swlist = []
    with open('stopword.txt','r') as sw:
        for line in sw:
            swlist.append(line.strip())
       
    with open('pn_en.dic','r') as f:
        wpdict = mkwpdict(swlist,f)

    with open('sentiment.txt','r') as sent:
        x,y,wlist = makexy(wpdict,sent)

    model = learning(x,y)
        
    return model

if __name__ == '__main__':
    model = main()
    
    
               
    
    
